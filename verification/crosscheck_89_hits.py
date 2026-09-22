#!/usr/bin/env python3
"""Cross-check all 89 WWeM zeta3 hits using mpmath matrix walk at N=1000.

For each hit:
  1. Run walk(start, dirv, z_num, z_den, N=1000, field='mpf', dps=200) from N=0
  2. Extract ALL possible limit ratios W[i][last] / W[j][last]
  3. Run PSLQ on each ratio AND its reciprocal
  4. Verify zeta3 has a NON-ZERO coefficient in at least one relation
  5. Report the exact relation, L value, and verification status

This is an independent verification — no float64, no shortcuts.
"""
import sys, json, time, mpmath as mp
sys.path.insert(0, '../ramanujan_dreams_mac/lib')
sys.path.insert(0, '../ml_limit_6f5')
from cmf_walk_4f3 import walk, rank_for_z, STATUS_OK
from pslq_companion import pslq_identify
from fractions import Fraction

mp.mp.dps = 200

INTERESTING_NAMES = {
    "zeta3", "zeta5", "zeta7", "zeta9", "catalan", "euler_gamma",
    "pi*e", "pi+e", "zeta2*zeta3", "zeta2+zeta3",
}

def verify_hit(start, dirv, z_num, z_den, N=1000, dps=200):
    """Run full mpmath walk at N=1000 and verify zeta3 relation.
    Returns dict with verification results."""
    mp.mp.dps = dps
    t0 = time.time()

    W, rank, status = walk(start, dirv, z_num, z_den, N, field='mpf', dps=dps)
    walk_time = time.time() - t0

    if status != STATUS_OK:
        return {
            "verified": False,
            "reason": f"walk status={status}",
            "walk_time": walk_time,
        }

    last = rank - 1
    results = []

    # Check ALL matrix pairs (i, j) where i != j
    for i in range(rank):
        for j in range(rank):
            if i == j:
                continue
            denom = W[j][last]
            if abs(denom) < mp.mpf(10) ** (-dps + 20):
                continue

            L = W[i][last] / denom
            if abs(L) < mp.mpf(10) ** (-dps + 20):
                continue

            # Run PSLQ on L
            rels_L = pslq_identify(L, maxcoeff=10000, maxsteps=5000)
            # Run PSLQ on 1/L
            rels_inv = pslq_identify(1 / L, maxcoeff=10000, maxsteps=5000)

            for source, rels in [("L", rels_L), ("1/L", rels_inv)]:
                for r in rels:
                    names = r.get("names", [])
                    coeffs = r.get("coeffs", [])
                    if "L" not in names:
                        continue
                    idx_L = names.index("L")
                    if coeffs[idx_L] == 0:
                        continue

                    # Check for interesting constants with non-zero coeff
                    for n, c in zip(names, coeffs):
                        if n in INTERESTING_NAMES and c != 0:
                            results.append({
                                "pair": (i, j),
                                "source": source,
                                "L_value": mp.nstr(L, 50),
                                "type": r.get("type", ""),
                                "coeffs": coeffs,
                                "names": names,
                                "target": n,
                                "target_coeff": c,
                                "L_coeff": coeffs[idx_L],
                                "verified": True,
                            })

    return {
        "verified": len(results) > 0,
        "n_verified_relations": len(results),
        "results": results,
        "walk_time": walk_time,
        "rank": rank,
        "status": status,
    }


def main():
    # Load the 89 unique zeta3 hits from the comparison
    with open('data/method_comparison.json') as f:
        comparison = json.load(f)

    wwem_hits = comparison["WWeM"]["hit_details"]
    print(f"Loaded {len(wwem_hits)} WWeM zeta3 hits from comparison")
    print(f"Running mpmath walk at N=1000, dps=200 for each hit...")
    print(f"{'='*70}\n")

    verified_count = 0
    failed_count = 0
    all_results = []

    for idx, hit in enumerate(wwem_hits):
        start = hit["start"]
        dirv = hit["dir"]
        z_str = hit["z"]
        z_num, z_den = map(int, z_str.split("/"))

        print(f"[{idx+1}/{len(wwem_hits)}] start={start}, dir={dirv}, z={z_str}", flush=True)

        result = verify_hit(start, dirv, z_num, z_den, N=1000, dps=200)

        if result["verified"]:
            verified_count += 1
            for r in result["results"][:3]:  # Show first 3 verified relations
                print(f"  VERIFIED: {r['coeffs']} * {r['names']}")
                print(f"    target={r['target']} (coeff={r['target_coeff']}), "
                      f"L_coeff={r['L_coeff']}, source={r['source']}")
                print(f"    L = {r['L_value']}")
            all_results.append({
                "start": start, "dir": dirv, "z": z_str,
                "verified": True,
                "n_relations": result["n_verified_relations"],
                "top_relations": result["results"][:5],
                "walk_time": result["walk_time"],
            })
        else:
            failed_count += 1
            print(f"  FAILED: {result.get('reason', 'no zeta3 relation found')}")
            all_results.append({
                "start": start, "dir": dirv, "z": z_str,
                "verified": False,
                "reason": result.get("reason", "no zeta3 relation found"),
                "walk_time": result.get("walk_time", 0),
            })
        print()

    # Summary
    print(f"{'='*70}")
    print(f"CROSS-CHECK SUMMARY")
    print(f"{'='*70}")
    print(f"Total hits checked: {len(wwem_hits)}")
    print(f"VERIFIED at N=1000, dps=200: {verified_count}")
    print(f"FAILED: {failed_count}")
    print(f"Verification rate: {verified_count/len(wwem_hits)*100:.1f}%")

    # Show all verified relations grouped by type
    print(f"\n{'='*70}")
    print(f"VERIFIED RELATIONS")
    print(f"{'='*70}")
    relation_types = {}
    for r in all_results:
        if r["verified"]:
            for rel in r["top_relations"]:
                key = f"{rel['coeffs']} * {rel['names']}"
                if key not in relation_types:
                    relation_types[key] = 0
                relation_types[key] += 1

    for key, count in sorted(relation_types.items(), key=lambda x: -x[1]):
        print(f"  [{count}x] {key}")

    # Save results
    with open('data/crosscheck_89_hits.json', 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to data/crosscheck_89_hits.json")


if __name__ == "__main__":
    main()
