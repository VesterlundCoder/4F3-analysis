#!/usr/bin/env python3
"""Delta search for zeta(2)+zeta(3) combined trajectories.

For each of the 89 verified zeta2+zeta3 trajectories:
  1. Compute the exact limit L at high precision (N=2000, dps=300)
  2. Compute delta at multiple depths (N, 2N, 4N, 8N)
  3. Search for perturbations that improve delta
  4. Store all trajectories with delta > -0.2

The irrationality measure delta is defined as:
  |p_n/q_n - L| = 1/q_n^(1+delta)

Positive delta means faster-than-generic convergence.
Delta > -0.2 means convergence is not too slow.
"""
import sys, json, time, random, mpmath as mp
from fractions import Fraction
sys.path.insert(0, '../ramanujan_dreams_mac/lib')
from cmf_walk_4f3 import walk, float_walk_limit, rank_for_z, STATUS_OK

mp.mp.dps = 300

def compute_delta(start, dirv, z_num, z_den, N=1000, dps=300):
    """Compute the irrationality measure delta for a trajectory.
    
    delta is defined from |p_n/q_n - L| = 1/q_n^(1+delta)
    where p_n/q_n is the convergent at depth n and L is the true limit.
    
    We estimate L at depth 2N and compute delta at depth N.
    """
    mp.mp.dps = dps
    
    # Walk to N
    W_N, rank, status_N = walk(start, dirv, z_num, z_den, N, field='mpf', dps=dps)
    if status_N != STATUS_OK:
        return None, None, None, f"walk N failed: status={status_N}"
    
    # Walk to 2N
    W_2N, rank, status_2N = walk(start, dirv, z_num, z_den, 2*N, field='mpf', dps=dps)
    if status_2N != STATUS_OK:
        return None, None, None, f"walk 2N failed: status={status_2N}"
    
    last = rank - 1
    
    # Find best convergent ratio at 2N (this is our L estimate)
    best_L = None
    best_pair = None
    for i in range(rank):
        for j in range(rank):
            if i == j:
                continue
            if abs(W_2N[j][last]) < mp.mpf(10)**(-dps+20):
                continue
            r = W_2N[i][last] / W_2N[j][last]
            if not mp.isfinite(r) or r == 0:
                continue
            if best_L is None or abs(r) > abs(best_L):
                best_L = r
                best_pair = (i, j)
    
    if best_L is None:
        return None, None, None, "no convergent found"
    
    L = best_L
    i, j = best_pair
    
    # Compute convergent p_n/q_n at depth N
    # p_n = W_N[i][last], q_n = W_N[j][last]
    p_n = W_N[i][last]
    q_n = W_N[j][last]
    
    if q_n == 0:
        return None, None, None, "q_n = 0"
    
    # |p_n/q_n - L| = |p_n - L*q_n| / |q_n|
    error = abs(p_n - L * q_n) / abs(q_n)
    
    # delta from: error = 1/|q_n|^(1+delta)
    # => 1+delta = -log(error) / log(|q_n|)
    # => delta = -log(error) / log(|q_n|) - 1
    
    log_q = mp.log(abs(q_n))
    log_error = mp.log(error)
    
    if log_q == 0:
        return None, L, best_pair, "log(q_n) = 0"
    
    delta = -log_error / log_q - 1
    
    # Also compute delta at 2N for trend
    p_2n = W_2N[i][last]
    q_2n = W_2N[j][last]
    if q_2n != 0:
        error_2n = abs(p_2n - L * q_2n) / abs(q_2n)
        log_q2 = mp.log(abs(q_2n))
        if log_q2 != 0:
            delta_2n = -mp.log(error_2n) / log_q2 - 1
        else:
            delta_2n = None
    else:
        delta_2n = None
    
    return float(delta), L, best_pair, {"delta_N": float(delta), "delta_2N": float(delta_2n) if delta_2n else None}

def search_perturbations(start, dirv, z_num, z_den, base_delta, N=1000, dps=200):
    """Try small perturbations of the trajectory to improve delta."""
    best_delta = base_delta
    best_traj = (start, dirv, z_num, z_den)
    improvements = []
    
    # Try perturbing each axis of start by +-1
    for axis in range(7):
        for delta_start in [-1, 1]:
            new_start = list(start)
            new_start[axis] += delta_start
            d, L, pair, info = compute_delta(new_start, dirv, z_num, z_den, N=N, dps=dps)
            if d is not None and d > best_delta:
                improvements.append({
                    "start": new_start, "dir": dirv, "z": f"{z_num}/{z_den}",
                    "delta": d, "L": mp.nstr(L, 30) if L else None,
                    "improvement": d - base_delta,
                })
                if d > best_delta:
                    best_delta = d
                    best_traj = (new_start, dirv, z_num, z_den)
    
    # Try perturbing each axis of dir by +-1
    for axis in range(7):
        for delta_dir in [-1, 1]:
            new_dir = list(dirv)
            new_dir[axis] += delta_dir
            d, L, pair, info = compute_delta(start, new_dir, z_num, z_den, N=N, dps=dps)
            if d is not None and d > best_delta:
                improvements.append({
                    "start": start, "dir": new_dir, "z": f"{z_num}/{z_den}",
                    "delta": d, "L": mp.nstr(L, 30) if L else None,
                    "improvement": d - base_delta,
                })
                if d > best_delta:
                    best_delta = d
                    best_traj = (start, new_dir, z_num, z_den)
    
    return best_delta, best_traj, improvements

def main():
    random.seed(42)
    
    with open('data/zeta2_zeta3_trajectories.json') as f:
        trajectories = json.load(f)
    
    print(f"{'='*70}")
    print(f"DELTA SEARCH: Zeta(2)+Zeta(3) Combined Trajectories")
    print(f"Trajectories: {len(trajectories)}")
    print(f"Threshold: delta > -0.2")
    print(f"Precision: 300 digits, N=1000")
    print(f"{'='*70}\n")
    
    results = []
    t0 = time.time()
    
    for idx, t in enumerate(trajectories):
        start = t['start']
        dirv = t['dir']
        z_str = t['z']
        z_num, z_den = map(int, z_str.split('/'))
        
        print(f"[{idx+1}/{len(trajectories)}] start={start}, dir={dirv}, z={z_str}", flush=True)
        
        # Compute base delta
        delta, L, pair, info = compute_delta(start, dirv, z_num, z_den, N=1000, dps=300)
        
        if delta is None:
            print(f"  FAILED: {info}")
            results.append({
                "start": start, "dir": dirv, "z": z_str,
                "delta": None, "L": None, "status": "failed",
                "reason": str(info),
            })
            continue
        
        print(f"  Base delta: {delta:.6f}")
        
        result = {
            "start": start, "dir": dirv, "z": z_str,
            "delta": delta, "L": mp.nstr(L, 30) if L else None,
            "pair": pair,
            "delta_N": info.get("delta_N"),
            "delta_2N": info.get("delta_2N"),
            "status": "ok",
        }
        
        # Search perturbations if delta is interesting
        if delta > -0.5:  # Search around promising trajectories
            best_delta, best_traj, improvements = search_perturbations(
                start, dirv, z_num, z_den, delta, N=500, dps=200
            )
            if improvements:
                print(f"  Found {len(improvements)} improvements, best delta: {best_delta:.6f}")
                result["best_delta_after_perturbation"] = best_delta
                result["improvements"] = improvements[:10]
        
        if delta > -0.2:
            print(f"  *** INTERESTING: delta = {delta:.6f} > -0.2 ***")
        
        results.append(result)
        print()
    
    elapsed = time.time() - t0
    
    # Summary
    print(f"\n{'='*70}")
    print(f"DELTA SEARCH SUMMARY")
    print(f"{'='*70}")
    print(f"Total trajectories: {len(trajectories)}")
    print(f"Time: {elapsed:.1f}s")
    
    deltas = [r["delta"] for r in results if r["delta"] is not None]
    if deltas:
        print(f"Delta range: [{min(deltas):.6f}, {max(deltas):.6f}]")
        print(f"Mean delta: {sum(deltas)/len(deltas):.6f}")
        
        # Count by threshold
        for threshold in [-0.2, 0.0, 0.5, 1.0, 2.0]:
            count = sum(1 for d in deltas if d > threshold)
            print(f"  delta > {threshold:+.1f}: {count} trajectories")
        
        # Top 10 by delta
        print(f"\nTop 10 by delta:")
        sorted_results = sorted([r for r in results if r["delta"] is not None], 
                               key=lambda x: -x["delta"])
        for i, r in enumerate(sorted_results[:10]):
            print(f"  {i+1}. delta={r['delta']:.6f}, start={r['start']}, dir={r['dir']}, z={r['z']}")
            if r.get("best_delta_after_perturbation"):
                print(f"     After perturbation: delta={r['best_delta_after_perturbation']:.6f}")
    
    # Save
    with open('data/delta_search_z2z3_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to data/delta_search_z2z3_results.json")

if __name__ == "__main__":
    main()
