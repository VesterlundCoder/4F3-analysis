# WWeM 4F3 CMF — 89 Verified Zeta(3) Limit Relations

## Cross-Check Verification

All 89 hits were independently verified using mpmath matrix walks at **N=1000 with 200-digit precision**,
starting from N=0 for each run. **100% verification rate (89/89).**

Each relation is a PSLQ-verified integer relation of the form:
```
c0*1 + c1*L + c2*pi^2 + c3*zeta(3) = 0
```
Solved for L:
```
L = -(c0 + c2*pi^2 + c3*zeta(3)) / c1
```

This means the limit L of the 4F3 CMF walk is an **exact rational linear combination of 1, zeta(2), and zeta(3)**.
(Since zeta(2) = pi^2/6, relations with pi^2 are equivalently zeta(2) relations.)

---

## All 89 Verified Hits

### Hit 1

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-4, 0, 3, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 2

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-1, 1, 0, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 3

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 2, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 4

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-2, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 5

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-4, 3, 2, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 6

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-4, 2, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 7

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-2, 4, 0, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 8

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-3, 3, 4, 2, 0, 1, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 9

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 10

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-2, 4, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 11

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-2, 1, 1, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 12

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 3]`, dir=`[-4, 3, 2, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 13

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 2, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 14

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-2, 3, 3, 2, 0, 1, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 15

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 2]`, dir=`[-3, 3, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -281/2 + 270*zeta2 - 252*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-281}{2} + 45 \, \\pi^2 -252 \, \zeta(3) $`

- L = 1.40083793372890922217833229001
- Target: `zeta3` (coefficient = 504)
- L coefficient: 2
- Source: 1/L

**Relation (alt 1):** `[455, 4, -90, 360] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -455/4 + 45/2*pi^2 - 90*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -455/4 + 135*zeta2 - 90*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-455}{4} + \frac{45}{2} \, \\pi^2 -90 \, \zeta(3) $`

- L = 7.63488512534295045506553257501
- Target: `zeta3` (coefficient = 360)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = -281/2 + 270*zeta2 - 252*zeta3

LaTeX: `$ L = \frac{-281}{2} + 45 \, \\pi^2 -252 \, \zeta(3) $`

- L = 0.713858452803377926818078293541
- Target: `zeta3` (coefficient = 504)
- L coefficient: 2
- Source: L

---

### Hit 16

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 3]`, dir=`[-3, 2, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 17

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-2, 3, 4, 2, 1, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 18

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-3, 3, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 19

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-4, 4, 4, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 20

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-2, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 21

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-4, 4, 2, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 22

**Trajectory:** start=`[0, 3, 3, 4, 3, 3, 3]`, dir=`[-3, 2, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 23

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 3]`, dir=`[-4, 2, 3, 3, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 24

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 3]`, dir=`[-4, 3, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 25

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 2, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 26

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-165, -24, 4, 120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -55/8 + 1/6*pi^2 + 5*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -55/8 + zeta2 + 5*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-55}{8} + \frac{1}{6} \, \\pi^2 + 5 \, \zeta(3) $`

- L = 1.28169210813768249638234308528
- Target: `zeta3` (coefficient = 120)
- L coefficient: -24
- Source: 1/L

**Relation (alt 1):** `[9, 4, -8] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = -8)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[-9, -4, 8, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

---

### Hit 27

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-1, 0, 1, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 28

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-2, 3, 2, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 29

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 2]`, dir=`[-3, 1, 4, 2, 0, 0, 1]`, z=`1/1`

**Relation (primary):** `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -281/2 + 270*zeta2 - 252*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-281}{2} + 45 \, \\pi^2 -252 \, \zeta(3) $`

- L = 1.40083793372890922217833229001
- Target: `zeta3` (coefficient = 504)
- L coefficient: 2
- Source: 1/L

**Relation (alt 1):** `[455, 4, -90, 360] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -455/4 + 45/2*pi^2 - 90*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -455/4 + 135*zeta2 - 90*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-455}{4} + \frac{45}{2} \, \\pi^2 -90 \, \zeta(3) $`

- L = 7.63488512534295045506553257501
- Target: `zeta3` (coefficient = 360)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = -281/2 + 270*zeta2 - 252*zeta3

LaTeX: `$ L = \frac{-281}{2} + 45 \, \\pi^2 -252 \, \zeta(3) $`

- L = 0.713858452803377926818078293541
- Target: `zeta3` (coefficient = 504)
- L coefficient: 2
- Source: L

---

### Hit 30

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 2]`, dir=`[-2, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -281/2 + 270*zeta2 - 252*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-281}{2} + 45 \, \\pi^2 -252 \, \zeta(3) $`

- L = 1.40083793372890922217833229001
- Target: `zeta3` (coefficient = 504)
- L coefficient: 2
- Source: 1/L

**Relation (alt 1):** `[455, 4, -90, 360] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -455/4 + 45/2*pi^2 - 90*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -455/4 + 135*zeta2 - 90*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-455}{4} + \frac{45}{2} \, \\pi^2 -90 \, \zeta(3) $`

- L = 7.63488512534295045506553257501
- Target: `zeta3` (coefficient = 360)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = -281/2 + 270*zeta2 - 252*zeta3

LaTeX: `$ L = \frac{-281}{2} + 45 \, \\pi^2 -252 \, \zeta(3) $`

- L = 0.713858452803377926818078293541
- Target: `zeta3` (coefficient = 504)
- L coefficient: 2
- Source: L

---

### Hit 31

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-3, 2, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 32

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-2, 0, 0, 4, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 33

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-3, 2, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 34

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-4, 3, 3, 2, 0, 0, 1]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 35

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 3]`, dir=`[-2, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 36

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-3, 2, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-165, -24, 4, 120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -55/8 + 1/6*pi^2 + 5*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -55/8 + zeta2 + 5*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-55}{8} + \frac{1}{6} \, \\pi^2 + 5 \, \zeta(3) $`

- L = 1.28169210813768249638234308528
- Target: `zeta3` (coefficient = 120)
- L coefficient: -24
- Source: 1/L

**Relation (alt 1):** `[-9, -4, 8] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

**Relation (alt 2):** `[-9, -4, 8, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

---

### Hit 37

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 3]`, dir=`[-4, 2, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 38

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-3, 4, 5, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 39

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-2, 4, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 40

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 3]`, dir=`[-4, 2, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 41

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-4, 3, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 42

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-3, 1, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 43

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 3]`, dir=`[-3, 3, 4, 2, 1, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 44

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-2, 0, 0, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 45

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-4, 4, 2, 2, 0, 0, 1]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 46

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-2, 4, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 47

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-4, 1, 3, 4, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 48

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-4, 1, 3, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 49

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-3, 2, 1, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 50

**Trajectory:** start=`[0, 5, 3, 3, 3, 3, 3]`, dir=`[-3, 4, 4, 3, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 437/8 - 81*zeta2 + 66*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{437}{8} + \frac{-27}{2} \, \\pi^2 + 66 \, \zeta(3) $`

- L = 1.38677753198635918881413218761
- Target: `zeta3` (coefficient = -528)
- L coefficient: 8
- Source: 1/L

**Relation (alt 1):** `[-61, 2, 12, -48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 61/2 - 6*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 61/2 - 36*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{61}{2} -6 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 7.59075107489381601028721830201
- Target: `zeta3` (coefficient = -48)
- L coefficient: 2
- Source: 1/L

**Relation (alt 2):** `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 437/8 - 81*zeta2 + 66*zeta3

LaTeX: `$ L = \frac{437}{8} + \frac{-27}{2} \, \\pi^2 + 66 \, \zeta(3) $`

- L = 0.721096193826881482117090161428
- Target: `zeta3` (coefficient = -528)
- L coefficient: 8
- Source: L

---

### Hit 51

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 52

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-4, 3, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 53

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-4, 4, 2, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 54

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-4, 3, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 55

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-4, 3, 2, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 56

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-3, 2, 1, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 57

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 1, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 58

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-4, 3, 2, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 59

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 2, 2, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 60

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-2, 3, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 61

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-3, 4, 2, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 62

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-1, 1, 1, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 63

**Trajectory:** start=`[0, 5, 4, 3, 3, 3, 3]`, dir=`[-3, 4, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[1431, -1, -180, 288] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 1431 - 180*pi^2 + 288*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 1431 - 1080*zeta2 + 288*zeta3

LaTeX: `$ \\frac{1}{L} = 1431 -180 \, \\pi^2 + 288 \, \zeta(3) $`

- L = 1.50694116567893519409120230554
- Target: `zeta3` (coefficient = 288)
- L coefficient: -1
- Source: 1/L

**Relation (alt 1):** `[4465, -8, -540, 720] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 4465/8 - 135/2*pi^2 + 90*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 4465/8 - 405*zeta2 + 90*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{4465}{8} + \frac{-135}{2} \, \\pi^2 + 90 \, \zeta(3) $`

- L = 8.94260726332632116412447187928
- Target: `zeta3` (coefficient = 720)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[1431, -1, -180, 288] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 1431 - 180*pi^2 + 288*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 1431 - 1080*zeta2 + 288*zeta3

LaTeX: `$ L = 1431 -180 \, \\pi^2 + 288 \, \zeta(3) $`

- L = 0.66359591387860280491621053759
- Target: `zeta3` (coefficient = 288)
- L coefficient: -1
- Source: L

---

### Hit 64

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 2, 3, 0, 0, 1]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 65

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-4, 1, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-165, -24, 4, 120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -55/8 + 1/6*pi^2 + 5*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -55/8 + zeta2 + 5*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-55}{8} + \frac{1}{6} \, \\pi^2 + 5 \, \zeta(3) $`

- L = 1.28169210813768249638234308528
- Target: `zeta3` (coefficient = 120)
- L coefficient: -24
- Source: 1/L

**Relation (alt 1):** `[-9, -4, 8] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

**Relation (alt 2):** `[-9, -4, 8, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

---

### Hit 66

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-165, -24, 4, 120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -55/8 + 1/6*pi^2 + 5*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -55/8 + zeta2 + 5*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-55}{8} + \frac{1}{6} \, \\pi^2 + 5 \, \zeta(3) $`

- L = 1.28169210813768249638234308528
- Target: `zeta3` (coefficient = 120)
- L coefficient: -24
- Source: 1/L

**Relation (alt 1):** `[-9, -4, 8] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

**Relation (alt 2):** `[-9, -4, 8, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -9/4 + 2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-9}{4} + 2 \, \zeta(3) $`

- L = 6.48871132239039964191026654282
- Target: `zeta3` (coefficient = 8)
- L coefficient: -4
- Source: 1/L

---

### Hit 67

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 3]`, dir=`[-3, 1, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 68

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 4, 4, 2, 0, 1, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 69

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-2, 3, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 70

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 4, 2, 0, 1, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 71

**Trajectory:** start=`[0, 5, 3, 3, 3, 3, 3]`, dir=`[-2, 4, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 437/8 - 81*zeta2 + 66*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{437}{8} + \frac{-27}{2} \, \\pi^2 + 66 \, \zeta(3) $`

- L = 1.38677753198635918881413218761
- Target: `zeta3` (coefficient = -528)
- L coefficient: 8
- Source: 1/L

**Relation (alt 1):** `[-61, 2, 12, -48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 61/2 - 6*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 61/2 - 36*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{61}{2} -6 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 7.59075107489381601028721830201
- Target: `zeta3` (coefficient = -48)
- L coefficient: 2
- Source: 1/L

**Relation (alt 2):** `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 437/8 - 81*zeta2 + 66*zeta3

LaTeX: `$ L = \frac{437}{8} + \frac{-27}{2} \, \\pi^2 + 66 \, \zeta(3) $`

- L = 0.721096193826881482117090161428
- Target: `zeta3` (coefficient = -528)
- L coefficient: 8
- Source: L

---

### Hit 72

**Trajectory:** start=`[0, 4, 3, 4, 3, 3, 3]`, dir=`[-3, 3, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 73

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-1, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 74

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-1, 4, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 75

**Trajectory:** start=`[0, 4, 3, 3, 2, 2, 3]`, dir=`[-3, 2, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[602, 1, -45, -132] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -602 + 45*pi^2 + 132*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -602 + 270*zeta2 + 132*zeta3

LaTeX: `$ \\frac{1}{L} = -602 + 45 \, \\pi^2 + 132 \, \zeta(3) $`

- L = 1.2442310200900755412868873309
- Target: `zeta3` (coefficient = -132)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[-220, -1, 15, 60] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -220 + 15*pi^2 + 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -220 + 90*zeta2 + 60*zeta3

LaTeX: `$ \\frac{1}{L} = -220 + 15 \, \\pi^2 + 60 \, \zeta(3) $`

- L = 5.97085485135678916932395260163
- Target: `zeta3` (coefficient = 60)
- L coefficient: -1
- Source: 1/L

**Relation (alt 2):** `[602, 1, -45, -132] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = -602 + 45*pi^2 + 132*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = -602 + 270*zeta2 + 132*zeta3

LaTeX: `$ L = -602 + 45 \, \\pi^2 + 132 \, \zeta(3) $`

- L = 0.803709266087583520317532313938
- Target: `zeta3` (coefficient = -132)
- L coefficient: 1
- Source: L

---

### Hit 76

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 2]`, dir=`[-2, 3, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 77

**Trajectory:** start=`[0, 4, 4, 3, 3, 3, 3]`, dir=`[-3, 2, 0, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ \\frac{1}{L} = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 1.44938565801514196461300791041
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: 1/L

**Relation (alt 1):** `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{269}{2} -18 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 8.25291594807718220914291319802
- Target: `zeta3` (coefficient = 72)
- L coefficient: -2
- Source: 1/L

**Relation (alt 2):** `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 315 - 270*zeta2 + 108*zeta3

LaTeX: `$ L = 315 -45 \, \\pi^2 + 108 \, \zeta(3) $`

- L = 0.68994749221504497561962644881
- Target: `zeta3` (coefficient = -108)
- L coefficient: 1
- Source: L

---

### Hit 78

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-2, 3, 4, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 79

**Trajectory:** start=`[0, 5, 3, 3, 3, 2, 3]`, dir=`[-3, 2, 0, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-1667, 12, -60, 1872] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 1667/12 + 5*pi^2 - 156*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 1667/12 + 30*zeta2 - 156*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{1667}{12} + 5 \, \\pi^2 -156 \, \zeta(3) $`

- L = 1.34442614105011903674429700103
- Target: `zeta3` (coefficient = 1872)
- L coefficient: 12
- Source: 1/L

**Relation (alt 1):** `[275, -12, 60, -720] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 275/12 + 5*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 275/12 + 30*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{275}{12} + 5 \, \\pi^2 -60 \, \zeta(3) $`

- L = 7.07841913158249998942655224556
- Target: `zeta3` (coefficient = -720)
- L coefficient: -12
- Source: 1/L

**Relation (alt 2):** `[-1667, 12, -60, 1872] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 1667/12 + 5*pi^2 - 156*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 1667/12 + 30*zeta2 - 156*zeta3

LaTeX: `$ L = \frac{1667}{12} + 5 \, \\pi^2 -156 \, \zeta(3) $`

- L = 0.743811779216751238479968470261
- Target: `zeta3` (coefficient = 1872)
- L coefficient: 12
- Source: L

---

### Hit 80

**Trajectory:** start=`[0, 4, 3, 3, 1, 3, 3]`, dir=`[-3, 4, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-551, -6, 30, 216] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -551/6 + 5*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -551/6 + 30*zeta2 + 36*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-551}{6} + 5 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 1.2678494407628345704749887818
- Target: `zeta3` (coefficient = 216)
- L coefficient: -6
- Source: 1/L

**Relation (alt 1):** `[-725, -24, 30, 360] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -725/24 + 5/4*pi^2 + 15*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -725/24 + 15/2*zeta2 + 15*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-725}{24} + \frac{5}{4} \, \\pi^2 + 15 \, \zeta(3) $`

- L = 6.26858182301773823556223686433
- Target: `zeta3` (coefficient = 360)
- L coefficient: -24
- Source: 1/L

**Relation (alt 2):** `[-551, -6, 30, 216] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = -551/6 + 5*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = -551/6 + 30*zeta2 + 36*zeta3

LaTeX: `$ L = \frac{-551}{6} + 5 \, \\pi^2 + 36 \, \zeta(3) $`

- L = 0.78873718585885403522969548046
- Target: `zeta3` (coefficient = 216)
- L coefficient: -6
- Source: L

---

### Hit 81

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-4, 4, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 82

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-5, 4, 0, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 83

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 3, 4, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 84

**Trajectory:** start=`[0, 4, 3, 3, 3, 3, 3]`, dir=`[-3, 4, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 1.35034320598534794086442369434
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{33}{8} + \frac{-3}{2} \, \\pi^2 + 9 \, \zeta(3) $`

- L = 7.18878698055719018897093834363
- Target: `zeta3` (coefficient = 72)
- L coefficient: -8
- Source: 1/L

**Relation (alt 2):** `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 3/2 - 18*zeta2 + 24*zeta3

LaTeX: `$ L = \frac{3}{2} -3 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 0.740552472562186993090242876646
- Target: `zeta3` (coefficient = 48)
- L coefficient: -2
- Source: L

---

### Hit 85

**Trajectory:** start=`[0, 3, 3, 3, 3, 3, 3]`, dir=`[-2, 4, 2, 3, 0, 0, 0]`, z=`-1/1`

**Relation (primary):** `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-41}{4} + \frac{1}{6} \, \\pi^2 + \frac{15}{2} \, \zeta(3) $`

- L = 2.43687969512747174209834915459
- Target: `zeta3` (coefficient = 90)
- L coefficient: -12
- Source: 1/L

**Relation (alt 1):** `[7, 4, -6] * ['1', 'L', 'zeta3'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

**Relation (alt 2):** `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = -7/4 + 3/2*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{-7}{4} + \frac{3}{2} \, \zeta(3) $`

- L = 18.8375872198506858137122219338
- Target: `zeta3` (coefficient = -6)
- L coefficient: 4
- Source: 1/L

---

### Hit 86

**Trajectory:** start=`[0, 4, 3, 3, 3, 2, 3]`, dir=`[-3, 4, 4, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 87

**Trajectory:** start=`[0, 5, 3, 3, 3, 3, 3]`, dir=`[-3, 4, 4, 1, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 437/8 - 81*zeta2 + 66*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{437}{8} + \frac{-27}{2} \, \\pi^2 + 66 \, \zeta(3) $`

- L = 1.38677753198635918881413218761
- Target: `zeta3` (coefficient = -528)
- L coefficient: 8
- Source: 1/L

**Relation (alt 1):** `[-61, 2, 12, -48] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 61/2 - 6*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 61/2 - 36*zeta2 + 24*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{61}{2} -6 \, \\pi^2 + 24 \, \zeta(3) $`

- L = 7.59075107489381601028721830201
- Target: `zeta3` (coefficient = -48)
- L coefficient: 2
- Source: 1/L

**Relation (alt 2):** `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   L = 437/8 - 81*zeta2 + 66*zeta3

LaTeX: `$ L = \frac{437}{8} + \frac{-27}{2} \, \\pi^2 + 66 \, \zeta(3) $`

- L = 0.721096193826881482117090161428
- Target: `zeta3` (coefficient = -528)
- L coefficient: 8
- Source: L

---

### Hit 88

**Trajectory:** start=`[0, 4, 3, 3, 2, 3, 3]`, dir=`[-2, 3, 2, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{205}{2} -3 \, \\pi^2 -60 \, \zeta(3) $`

- L = 1.30246897411966021784254585318
- Target: `zeta3` (coefficient = -120)
- L coefficient: -2
- Source: 1/L

**Relation (alt 1):** `[-29, 1, 24] * ['1', 'L', 'zeta3'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

**Relation (alt 2):** `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7'] = 0`

> 1/L = 29 - 24*zeta3

LaTeX: `$ \\frac{1}{L} = 29 -24 \, \zeta(3) $`

- L = 6.63859319920461227456015818117
- Target: `zeta3` (coefficient = 24)
- L coefficient: 1
- Source: 1/L

---

### Hit 89

**Trajectory:** start=`[0, 3, 3, 3, 2, 3, 3]`, dir=`[-4, 3, 3, 2, 0, 0, 0]`, z=`1/1`

**Relation (primary):** `[-189, 4, 12, 56] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 189/4 - 3*pi^2 - 14*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 189/4 - 18*zeta2 - 14*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{189}{4} -3 \, \\pi^2 -14 \, \zeta(3) $`

- L = 1.23093564948517656946924485848
- Target: `zeta3` (coefficient = 56)
- L coefficient: 4
- Source: 1/L

**Relation (alt 1):** `[69, -4, -24] * ['1', 'L', 'zeta2+zeta3'] = 0`

> 1/L = 69/4 - 6*(zeta2+zeta3)

LaTeX: `$ \\frac{1}{L} = \frac{69}{4} -6 \, (\zeta(2)+\zeta(3)) $`

- L = 5.95046193007053705296416990033
- Target: `zeta2+zeta3` (coefficient = -24)
- L coefficient: -4
- Source: 1/L

**Relation (alt 2):** `[69, -4, -4, -24] * ['1', 'L', 'pi^2', 'zeta3'] = 0`

> 1/L = 69/4 - pi^2 - 6*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 69/4 - 6*zeta2 - 6*zeta3

LaTeX: `$ \\frac{1}{L} = \frac{69}{4} -\\pi^2 -6 \, \zeta(3) $`

- L = 5.95046193007053705296416990033
- Target: `zeta3` (coefficient = -24)
- L coefficient: -4
- Source: 1/L

---


## Summary: Unique Relation Types

| Count | PSLQ Relation | Solved for L |
|------:|---------------|--------------|
| 50 | `[3, -2, -6, 48] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 3/2 - 3*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 3/2 - 18*zeta2 + 24*zeta3 |
| 50 | `[33, -8, -12, 72] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 33/8 - 3/2*pi^2 + 9*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 33/8 - 9*zeta2 + 9*zeta3 |
| 22 | `[205, -2, -6, -120] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 205/2 - 3*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 205/2 - 18*zeta2 - 60*zeta3 |
| 22 | `[-29, 1, 24] * ['1', 'L', 'zeta3']` | 1/L = 29 - 24*zeta3 |
| 22 | `[-29, 1, 24, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7']` | 1/L = 29 - 24*zeta3 |
| 22 | `[-29, 1, 0, 24] * ['1', 'L', 'pi^3', 'zeta3']` | 1/L = 29 - 24*zeta3 |
| 22 | `[-29, 1, 0, 24] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 29 - 24*zeta3 |
| 22 | `[-315, 1, 45, -108] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 315 - 45*pi^2 + 108*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 315 - 270*zeta2 + 108*zeta3 |
| 22 | `[269, -2, -36, 72] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 269/2 - 18*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 269/2 - 108*zeta2 + 36*zeta3 |
| 16 | `[-123, -12, 2, 90] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -41/4 + 1/6*pi^2 + 15/2*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -41/4 + zeta2 + 15/2*zeta3 |
| 16 | `[7, 4, -6] * ['1', 'L', 'zeta3']` | 1/L = -7/4 + 3/2*zeta3 |
| 16 | `[7, 4, -6, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7']` | 1/L = -7/4 + 3/2*zeta3 |
| 16 | `[7, 4, 0, -6] * ['1', 'L', 'pi^3', 'zeta3']` | 1/L = -7/4 + 3/2*zeta3 |
| 16 | `[7, 4, 0, -6] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -7/4 + 3/2*zeta3 |
| 6 | `[281, 2, -90, 504] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -281/2 + 45*pi^2 - 252*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -281/2 + 270*zeta2 - 252*zeta3 |
| 6 | `[455, 4, -90, 360] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -455/4 + 45/2*pi^2 - 90*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -455/4 + 135*zeta2 - 90*zeta3 |
| 6 | `[-437, 8, 108, -528] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 437/8 - 27/2*pi^2 + 66*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 437/8 - 81*zeta2 + 66*zeta3 |
| 6 | `[-61, 2, 12, -48] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 61/2 - 6*pi^2 + 24*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 61/2 - 36*zeta2 + 24*zeta3 |
| 4 | `[-165, -24, 4, 120] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -55/8 + 1/6*pi^2 + 5*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -55/8 + zeta2 + 5*zeta3 |
| 4 | `[-9, -4, 8, 0, 0] * ['1', 'L', 'zeta3', 'zeta5', 'zeta7']` | 1/L = -9/4 + 2*zeta3 |
| 3 | `[-9, -4, 8] * ['1', 'L', 'zeta3']` | 1/L = -9/4 + 2*zeta3 |
| 3 | `[-9, -4, 0, 8] * ['1', 'L', 'pi^3', 'zeta3']` | 1/L = -9/4 + 2*zeta3 |
| 3 | `[-9, -4, 0, 8] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -9/4 + 2*zeta3 |
| 2 | `[1431, -1, -180, 288] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 1431 - 180*pi^2 + 288*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 1431 - 1080*zeta2 + 288*zeta3 |
| 2 | `[4465, -8, -540, 720] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 4465/8 - 135/2*pi^2 + 90*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 4465/8 - 405*zeta2 + 90*zeta3 |
| 2 | `[602, 1, -45, -132] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -602 + 45*pi^2 + 132*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -602 + 270*zeta2 + 132*zeta3 |
| 2 | `[-220, -1, 15, 60] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -220 + 15*pi^2 + 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -220 + 90*zeta2 + 60*zeta3 |
| 2 | `[-1667, 12, -60, 1872] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 1667/12 + 5*pi^2 - 156*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 1667/12 + 30*zeta2 - 156*zeta3 |
| 2 | `[275, -12, 60, -720] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 275/12 + 5*pi^2 - 60*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 275/12 + 30*zeta2 - 60*zeta3 |
| 2 | `[-551, -6, 30, 216] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -551/6 + 5*pi^2 + 36*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -551/6 + 30*zeta2 + 36*zeta3 |
| 2 | `[-725, -24, 30, 360] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -725/24 + 5/4*pi^2 + 15*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = -725/24 + 15/2*zeta2 + 15*zeta3 |
| 2 | `[-189, 4, 12, 56] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 189/4 - 3*pi^2 - 14*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 189/4 - 18*zeta2 - 14*zeta3 |
| 2 | `[69, -4, -24] * ['1', 'L', 'zeta2+zeta3']` | 1/L = 69/4 - 6*(zeta2+zeta3) |
| 1 | `[9, 4, -8] * ['1', 'L', 'zeta3']` | 1/L = -9/4 + 2*zeta3 |
| 1 | `[9, 4, 0, -8] * ['1', 'L', 'pi^3', 'zeta3']` | 1/L = -9/4 + 2*zeta3 |
| 1 | `[9, 4, 0, -8] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = -9/4 + 2*zeta3 |
| 1 | `[69, -4, -4, -24] * ['1', 'L', 'pi^2', 'zeta3']` | 1/L = 69/4 - pi^2 - 6*zeta3

   equivalently (using zeta(2) = pi^2/6):

   1/L = 69/4 - 6*zeta2 - 6*zeta3 |

## Key Observations

1. **All 89 hits involve zeta(3)** with a non-zero coefficient — these are genuine zeta(3) limits.

2. **Since zeta(2) = pi^2/6**, every relation containing pi^2 is equivalently a zeta(2) relation.
   For example, the most common relation:
   ```
   1/L = 3/2 - 3*pi^2 + 24*zeta(3)
   ```
   is equivalently:
   ```
   1/L = 3/2 - 18*zeta(2) + 24*zeta(3)
   ```
   So every limit is a **rational linear combination of 1, zeta(2), and zeta(3)**.

3. **The simplest pure zeta(3) relation** (no zeta(2)/pi^2) is `[-29, 1, 24] * [1, L, zeta3] = 0`:
   ```
   1/L = 29 - 24*zeta(3)
   L   = 1 / (29 - 24*zeta(3))
   ```
   Found in 22 trajectories.

4. **Another pure zeta(3) relation** is `[7, 4, -6] * [1, L, zeta3] = 0`:
   ```
   1/L = -7/4 + 3/2*zeta(3)
   L   = 1 / (-7/4 + 3/2*zeta(3))
   ```
   Found in 16 trajectories.

5. **The most common relation** is `[3, -2, -6, 48] * [1, L, pi^2, zeta3] = 0`:
   ```
   1/L = 3/2 - 3*pi^2 + 24*zeta(3)
      = 3/2 - 18*zeta(2) + 24*zeta(3)   (using zeta(2) = pi^2/6)
   L   = 1 / (3/2 - 18*zeta(2) + 24*zeta(3))
   ```
   Found in 50 of the 89 trajectories.

6. **Hit #89** found a **zeta(2)+zeta(3)** relation:
   ```
   1/L = 69/4 - 6*(zeta(2)+zeta(3))
   L   = 1 / (69/4 - 6*(zeta(2)+zeta(3)))
   ```

7. All limits are **rational linear combinations of 1, zeta(2), and zeta(3)** —
   the 4F3 CMF naturally produces zeta(2) and zeta(3) in specific trajectory families.
   The PSLQ relations are typically found on 1/L rather than L directly.

8. **Comparison to brute force:** Pure random search (2,000 candidates) found 0 hits.
   Brute force grid search (2,000 candidates) found 0 hits.
   WWeM (2,000 candidates) found 89 unique hits — a 4.45% hit rate vs 0% for both baselines.