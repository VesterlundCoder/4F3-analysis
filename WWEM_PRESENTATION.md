# WWeM: WorldWestMath — A World Model AI for Mathematical Discovery

## What is WWeM?

WWeM (WorldWestMath) is a world-model AI that explores mathematical environments the way a robot explores a physical world. Instead of pixels and physics, WWeM navigates the **Conservative Matrix Field (CMF)** — a lattice of matrix transformations whose limits converge to mathematical constants like ζ(3), π², and Catalan's constant.

The core idea: treat mathematical search as a **reinforcement learning problem** in a structured space. The "world" is the CMF lattice. The "actions" are trajectory choices (start point + direction + z-parameter). The "observations" are the limits these trajectories converge to. The "dream" is the learned model that predicts which trajectories will produce interesting constants.

## The 4F3 CMF World

The current world is the **4F3 Conservative Matrix Field**:
- **4** numerator roots (x_i) + **3** denominator roots (y_j) = 7 axes
- **Rank 4** matrix walk (rank 3 when z=1)
- Each trajectory is defined by: start point (7 integers), direction (7 integers), z-value (rational)
- The walk produces a sequence of matrix products whose ratios converge to a limit L
- PSLQ integer relation detection identifies L as a combination of known constants

This is the same framework used by the [Ramanujan Machine project](https://www.ramanujanmachine.com/), implemented using their [ramanujantools](https://github.com/RamanujanMachine/ramanujantools) algorithms.

## How WWeM Was Trained

### Phase 1: Corpus Building
1. **11,067 4F3 CMF hits** were pre-computed using brute-force and random search
2. These were **PSLQ-verified** at high precision (200+ digits) to confirm genuine mathematical relations
3. The verified hits were compiled into a **training corpus of 9,865 samples**

### Phase 2: WestMath Model Fine-Tuning
1. **WestMath124M** — a 124M parameter transformer model (85,889,280 parameters) — was fine-tuned on the verified 4F3 corpus
2. The model learns to predict which trajectory parameters (start, direction, z) produce convergent walks with interesting limits
3. Checkpoint: `ml_limit_6f5/reports/structured_verified/finetuned/best.pt`

### Phase 3: World Model Loop
WWeM runs a continuous loop:
1. **Generate** 10,000 candidate trajectories per round (mix of seeded, model-guided, and random)
2. **Evaluate** each candidate with the CMF oracle (float walk → convergence check)
3. **Verify** target-close candidates with high-precision PSLQ (120-200 digits)
4. **Retrain** the model on all verified data every 5 rounds
5. **Repeat** for up to 500 rounds

The generation mix:
- 20% zeta3-seeded (perturbations of known zeta3-producing trajectories)
- 20% PSLQ-verified-seeded (perturbations of all verified discoveries)
- 20% corpus-guided (WestMath-informed perturbations)
- 40% random exploration (wide parameter ranges)

## Hit Rate Results

### WWeM vs Brute Force vs Random (2,000 candidates each)

| Method | Valid Walks | Zeta(3) Hits | Unique Hits | Hit Rate |
|--------|------------:|-------------:|------------:|---------:|
| Pure Random | 9 | 0 | **0** | 0.00% |
| Brute Force | 0 | 0 | **0** | 0.00% |
| **WWeM** | 672 | 996 | **89** | **4.45%** |

### Cross-Verification
All 89 WWeM hits were independently verified using mpmath matrix walks at **N=1000 with 200-digit precision**:
- **Verification rate: 100% (89/89)**
- Every hit has a non-zero ζ(3) coefficient in its PSLQ relation
- All limits are rational linear combinations of 1, ζ(2), and ζ(3)

### 100K Run (in progress)
- 110 genuine hits in first 1,000 candidates (11% hit rate with PSLQ-verified seeds)
- Running continuously to evaluate all 100,000 candidates

### Main World Model (running)
- Round 3, Phase 2 (Delta Maximization)
- 79 unique zeta/catalan hits
- 2,350+ PSLQ-verified relations
- 1,881 total zeta/catalan entries

## Key Discoveries

### Pure Zeta(3) Relations (no ζ(2) mixing)
```
1/L = 29 - 24·ζ(3)              (22 trajectories)
1/L = -7/4 + 3/2·ζ(3)          (16 trajectories)
1/L = -9/4 + 2·ζ(3)            (3 trajectories)
```

### Zeta(2)+Zeta(3) Combined Relations
```
1/L = 3/2 - 18·ζ(2) + 24·ζ(3)  (50 trajectories — most common)
1/L = -41/4 + ζ(2) + 15/2·ζ(3) (16 trajectories)
1/L = 205/2 - 18·ζ(2) - 60·ζ(3) (22 trajectories)
1/L = 69/4 - 6·(ζ(2)+ζ(3))     (2 trajectories — explicit combined form)
```

### Significance
The ζ(2)+ζ(3) combined relations are particularly interesting because:
- **No proof of irrationality exists for ζ(2)+ζ(3)** as a combined constant
- The 4F3 CMF naturally produces this combination in specific trajectory families
- Positive-delta trajectories would provide evidence of algebraic independence

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    WWeM World Model                      │
│                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────┐    │
│  │ WestMath │───▶│ Candidate│───▶│ CMF Oracle Walk  │    │
│  │  124M    │    │ Generator│    │ (mpmath, N=1000) │    │
│  │ (finetuned)  └──────────┘    └────────┬─────────┘    │
│  └────▲────┘                            │               │
│       │                                 ▼               │
│  ┌────┴────┐                     ┌──────────────┐       │
│  │ Retrain │◀────────────────────│ PSLQ Verify  │       │
│  │ (every  │                     │ (200 digits) │       │
│  │  5 rds) │                     └──────┬───────┘       │
│  └─────────┘                            │               │
│                                         ▼               │
│                                  ┌──────────────┐       │
│                                  │  Dashboard    │       │
│                                  │ localhost:8080│       │
│                                  └──────────────┘       │
└─────────────────────────────────────────────────────────┘
```

## Files

- `world_model_4f3.py` — Main world model loop with dashboard
- `crosscheck_89_hits.py` — Independent verification script (mpmath N=1000, 200 digits)
- `compare_methods.py` — WWeM vs Random vs Brute Force comparison
- `delta_search_z2z3.py` — Delta search for zeta(2)+zeta(3) trajectories
- `wwem_100k.py` — 100,000 candidate evaluation run
- `data/verified_89_hits.md` — All 89 verified hits with full relations
- `data/crosscheck_89_hits.json` — Raw verification data

## References

- [Ramanujan Machine](https://www.ramanujanmachine.com/)
- [ramanujantools](https://github.com/RamanujanMachine/ramanujantools)
- [Conservative Matrix Fields](https://arxiv.org/abs/2207.10326)
- [DreamerV3](https://arxiv.org/abs/2301.04104) — inspiration for world-model architecture
