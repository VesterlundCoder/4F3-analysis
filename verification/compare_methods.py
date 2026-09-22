#!/usr/bin/env python3
"""Fair comparison: WWeM vs Pure Random vs Brute Force grid search.
All three use the same oracle (float_walk_limit) and PSLQ verification.
Each method gets the SAME compute budget (N candidates)."""
import sys, time, random, json, math, itertools
sys.path.insert(0, 'ramanujan_dreams_mac/lib')
sys.path.insert(0, 'ml_limit_6f5')
from cmf_walk_4f3 import walk, float_walk_limit
from pslq_companion import pslq_identify
import mpmath as mp

mp.mp.dps = 100

INTERESTING_NAMES = {
    "zeta3", "zeta5", "zeta7", "zeta9", "catalan", "euler_gamma",
    "pi*e", "pi+e", "zeta2*zeta3", "zeta2+zeta3",
}

def is_rational_L(L, tol=1e-10):
    if L is None or math.isnan(L) or abs(L) < 1e-15:
        return True
    for denom in range(1, 200):
        num = round(L * denom)
        if abs(L - num/denom) < tol:
            return True
    return False

def check_zeta3_pslq(start, dirv, z_num, z_den, N=500, dps=80):
    """Run high-precision PSLQ and return list of interesting relations."""
    try:
        W, rank, status = walk(start, dirv, z_num, z_den, N, field='mpf', dps=dps)
        if status != 0 or rank < 2:
            return []
        last = rank - 1
        hits = []
        for i in range(rank):
            for j in range(rank):
                if i == j or W[j][last] == 0:
                    continue
                L = W[i][last] / W[j][last]
                if abs(L) < mp.mpf(10)**(-70):
                    continue
                for Lval in [L, 1/L]:
                    rels = pslq_identify(Lval, maxcoeff=10000, maxsteps=3000)
                    for r in rels:
                        names = r.get("names", [])
                        coeffs = r.get("coeffs", [])
                        if "L" not in names:
                            continue
                        idx_L = names.index("L")
                        if coeffs[idx_L] == 0:
                            continue
                        for n, c in zip(names, coeffs):
                            if n in INTERESTING_NAMES and c != 0:
                                hits.append({
                                    "coeffs": coeffs, "names": names,
                                    "type": r.get("type", ""),
                                    "target": n,
                                })
                                break
        return hits
    except:
        return []

def evaluate_candidate(start, dirv, z_num, z_den, N=500):
    """Evaluate one candidate: float walk → check if near target → PSLQ."""
    try:
        L, status, conv = float_walk_limit(start, dirv, z_num, z_den, N=N)
        if status != 0 or L is None or math.isnan(L):
            return None, None
        if is_rational_L(L):
            return L, []
        # Run PSLQ
        hits = check_zeta3_pslq(start, dirv, z_num, z_den, N=N, dps=80)
        return L, hits
    except:
        return None, None

# ── Method 1: Pure Random ──────────────────────────────────────────
def method_random(n_candidates, seed=42):
    random.seed(seed)
    results = []
    for _ in range(n_candidates):
        start = [random.randint(-8, 8) for _ in range(7)]
        dirv = [random.randint(-4, 4) for _ in range(7)]
        z_choices = [(1,1), (-1,1), (1,2), (-1,2), (1,3), (-1,3), (1,4), (-1,4),
                    (1,5), (-1,5), (1,6), (-1,6), (1,7), (-1,7), (1,8), (-1,8),
                    (1,12), (-1,12), (1,16), (-1,16), (1,24), (-1,24)]
        z_num, z_den = random.choice(z_choices)
        results.append((start, dirv, z_num, z_den))
    return results

# ── Method 2: Brute Force (systematic grid) ───────────────────────
def method_bruteforce(n_candidates):
    """Systematic grid search over small parameter space."""
    # Grid: start in [-3,3]^7, dir in [-2,2]^7, z in small set
    # This is a huge space, so we sample systematically
    results = []
    start_range = range(-3, 4)  # -3 to 3
    dir_range = range(-2, 3)    # -2 to 2
    z_choices = [(1,1), (-1,1), (1,2), (-1,2), (1,3), (-1,3), (1,4), (-1,4)]

    # Systematic: vary first 3 components of start and dir, fix rest to 3
    for s0 in start_range:
        for s1 in start_range:
            for s2 in start_range:
                for d0 in dir_range:
                    for d1 in dir_range:
                        for d2 in dir_range:
                            for z_num, z_den in z_choices:
                                start = [s0, s1, s2, 3, 3, 3, 3]
                                dirv = [d0, d1, d2, 0, 0, 0]
                                results.append((start, dirv, z_num, z_den))
                                if len(results) >= n_candidates:
                                    return results
    return results

# ── Method 3: WWeM (WestMath-guided + zeta3 seeds) ─────────────────
def method_wwem(n_candidates, seed=42):
    """WWeM: 20% zeta3-seeded, 30% guided (corpus-perturbed), 50% random."""
    random.seed(seed)

    # Load zeta3 seeds
    with open('wwem_4f3/data/zeta3_seeds.json') as f:
        z3seeds = json.load(f)

    # Load training corpus for guided generation
    corpus = []
    with open('wwem_4f3/data/training_corpus.jsonl') as f:
        for line in f:
            corpus.append(json.loads(line))

    results = []
    n_seeded = int(n_candidates * 0.2)
    n_guided = int(n_candidates * 0.3)
    n_random = n_candidates - n_seeded - n_guided

    # Seeded: perturb zeta3 seeds
    for _ in range(n_seeded):
        seed = random.choice(z3seeds)
        start, dirv, z_num, z_den = list(seed[0]), list(seed[1]), seed[2], seed[3]
        # Small perturbation
        for _ in range(random.randint(1, 2)):
            axis = random.randint(0, 6)
            start[axis] += random.choice([-1, 0, 1])
        for _ in range(random.randint(0, 1)):
            axis = random.randint(0, 6)
            dirv[axis] += random.choice([-1, 0, 1])
        if random.random() < 0.1:
            z_choices = [(1,1), (-1,1), (1,2), (-1,2), (1,3), (-1,3), (1,4), (-1,4)]
            z_num, z_den = random.choice(z_choices)
        results.append((start, dirv, z_num, z_den))

    # Guided: perturb corpus entries
    for _ in range(n_guided):
        entry = random.choice(corpus)
        start = list(entry["start"])
        dirv = list(entry["dir"])
        z_num, z_den = entry["z_num"], entry["z_den"]
        for _ in range(random.randint(1, 3)):
            axis = random.randint(0, 6)
            start[axis] += random.choice([-2, -1, 0, 1, 2])
        if random.random() < 0.4:
            axis = random.randint(0, 6)
            dirv[axis] += random.choice([-2, -1, 0, 1, 2])
        results.append((start, dirv, z_num, z_den))

    # Random (same distribution as method_random)
    for _ in range(n_random):
        start = [random.randint(-8, 8) for _ in range(7)]
        dirv = [random.randint(-4, 4) for _ in range(7)]
        z_choices = [(1,1), (-1,1), (1,2), (-1,2), (1,3), (-1,3), (1,4), (-1,4),
                    (1,5), (-1,5), (1,6), (-1,6), (1,7), (-1,7), (1,8), (-1,8),
                    (1,12), (-1,12), (1,16), (-1,16), (1,24), (-1,24)]
        z_num, z_den = random.choice(z_choices)
        results.append((start, dirv, z_num, z_den))

    return results

# ── Run comparison ─────────────────────────────────────────────────
N_CANDIDATES = 2000  # Same budget for each method

print(f"{'='*70}")
print(f"COMPARISON: WWeM vs Pure Random vs Brute Force")
print(f"Budget: {N_CANDIDATES} candidates each")
print(f"{'='*70}\n")

methods = {
    "Pure Random": method_random,
    "Brute Force": method_bruteforce,
    "WWeM": method_wwem,
}

all_results = {}

for method_name, method_fn in methods.items():
    print(f"\n{'─'*50}")
    print(f"Method: {method_name}")
    print(f"{'─'*50}")

    t0 = time.time()
    candidates = method_fn(N_CANDIDATES)
    gen_time = time.time() - t0

    n_valid = 0
    n_zc_hits = 0
    unique_zc = set()
    hit_details = []
    valid_Ls = []

    t0 = time.time()
    for idx, (start, dirv, z_num, z_den) in enumerate(candidates):
        if (idx + 1) % 200 == 0:
            print(f"  [{idx+1}/{N_CANDIDATES}] valid={n_valid}, zc_hits={n_zc_hits}, "
                  f"unique={len(unique_zc)}", flush=True)

        L, hits = evaluate_candidate(start, dirv, z_num, z_den, N=500)

        if L is not None:
            n_valid += 1
            valid_Ls.append(L)

        if hits:
            n_zc_hits += len(hits)
            key = (tuple(start), tuple(dirv), z_num, z_den)
            if key not in unique_zc:
                unique_zc.add(key)
                hit_details.append({
                    "start": start, "dir": dirv, "z": f"{z_num}/{z_den}",
                    "L": L, "hits": hits,
                })

    eval_time = time.time() - t0

    all_results[method_name] = {
        "n_candidates": N_CANDIDATES,
        "n_valid": n_valid,
        "valid_rate": n_valid / N_CANDIDATES,
        "n_zc_hits": n_zc_hits,
        "n_unique_zc": len(unique_zc),
        "hit_rate": len(unique_zc) / N_CANDIDATES,
        "gen_time": gen_time,
        "eval_time": eval_time,
        "total_time": gen_time + eval_time,
        "hits_per_second": len(unique_zc) / (gen_time + eval_time) if (gen_time + eval_time) > 0 else 0,
        "hit_details": hit_details,
    }

    print(f"\n  Results:")
    print(f"    Valid: {n_valid}/{N_CANDIDATES} ({n_valid/N_CANDIDATES*100:.1f}%)")
    print(f"    ZC hits (total): {n_zc_hits}")
    print(f"    Unique ZC trajectories: {len(unique_zc)}")
    print(f"    Hit rate: {len(unique_zc)/N_CANDIDATES*100:.2f}%")
    print(f"    Time: {gen_time + eval_time:.1f}s")
    print(f"    Hits/sec: {len(unique_zc)/(gen_time + eval_time):.4f}")

    if hit_details:
        print(f"\n  Sample hits:")
        for h in hit_details[:5]:
            for hit in h["hits"][:2]:
                print(f"    {hit['coeffs']} * {hit['names']} (target: {hit['target']})")
            print(f"      start={h['start']}, dir={h['dir']}, z={h['z']}, L={h['L']:.10f}")

# ── Summary table ──────────────────────────────────────────────────
print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"{'Method':<15} {'Valid':>8} {'Hits':>6} {'Unique':>8} {'Rate%':>7} {'Time':>8} {'Hits/s':>8}")
print(f"{'─'*15} {'─'*8} {'─'*6} {'─'*8} {'─'*7} {'─'*8} {'─'*8}")
for name, r in all_results.items():
    print(f"{name:<15} {r['n_valid']:>8} {r['n_zc_hits']:>6} {r['n_unique_zc']:>8} "
          f"{r['hit_rate']*100:>6.2f}% {r['total_time']:>7.1f}s {r['hits_per_second']:>8.4f}")

# Save results
with open('wwem_4f3/data/method_comparison.json', 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nResults saved to wwem_4f3/data/method_comparison.json")
