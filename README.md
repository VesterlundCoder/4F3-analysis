# 4F3 CMF Analysis — WWeM World Model Results

This repository contains the verified results from WWeM (WorldWestMath), a world-model AI that discovers mathematical constants by navigating the 4F3 Conservative Matrix Field.

## Key Results

- **89 unique trajectories** producing verified ζ(3) limits
- **100% verification rate** (89/89) at N=1000 with 200-digit precision
- **4.45% hit rate** vs 0% for both pure random and brute-force search
- All limits are rational linear combinations of **1, ζ(2), and ζ(3)**
- ζ(2)+ζ(3) combined relations found — significant because no irrationality proof exists for this combination

## Files

### Results
- `verified_89_hits.md` — All 89 verified hits with full PSLQ relations, numerical values, and LaTeX
- `results/crosscheck_89_hits.json` — Raw verification data
- `results/method_comparison.json` — WWeM vs Random vs Brute Force comparison

### Verification Code
- `verification/crosscheck_89_hits.py` — Independent verification script (mpmath N=1000, 200 digits)
- `verification/compare_methods.py` — WWeM vs Random vs Brute Force comparison
- `verification/delta_search_z2z3.py` — Delta (irrationality measure) search for ζ(2)+ζ(3) trajectories
- `verification/cmf_walk_4f3.py` — 4F3 CMF matrix walk implementation (matches ramanujantools)
- `verification/pslq_companion.py` — PSLQ integer relation detection

### Documentation
- `WWEM_PRESENTATION.md` — Overview of WWeM architecture, training, and results

## How to Verify

```bash
# Install dependencies
pip install mpmath

# Run the cross-check (takes ~30 minutes)
cd verification
python3 crosscheck_89_hits.py
```

## Architecture

WWeM uses:
- **WestMath124M** — a 124M parameter transformer fine-tuned on 9,865 PSLQ-verified 4F3 samples
- **CMF Oracle** — mpmath matrix walk at N=1000 with 200-digit precision
- **PSLQ** — integer relation detection for identifying limits as combinations of known constants
- **Dashboard** — real-time monitoring at http://localhost:8080

## References

- [Ramanujan Machine](https://www.ramanujanmachine.com/)
- [ramanujantools](https://github.com/RamanujanMachine/ramanujantools)
- [Conservative Matrix Fields paper](https://arxiv.org/abs/2207.10326)
