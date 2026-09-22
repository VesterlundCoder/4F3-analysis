"""
cmf_walk_4f3.py
===============
CORRECTED Ramanujan Dreams 4F3 CMF trajectory walk - reference oracle.

4F3 = 4 numerator roots (x_i) + 3 denominator roots (y_j), 7 axes, rank 4.

Semantics (matching upstream ramanujantools Matrix.walk):

  Start point: the 4F3 data stores position directly (not shift).
      x_i = start[i]        (i = 0..3)   numerator roots
      y_j = start[4+j]      (j = 0..2)   denominator roots

  Theta differential operator:
      D(theta) = theta * prod_j (theta + y_j - 1)  -  z * prod_i (theta + x_i)
               = d_0 + d_1 theta + ... + d_r theta^r
  Rank r = 4 for z != 1, r = 3 for z = 1 (d_4 = 1 - z).
  Monic companion C(v): subdiagonal ones, last column c_i = -d_i / d_r.

  Axis operators (I + C/a), four cases:
      x_i +1 : A =  I + C(v)/x_i            then x_i += 1
      x_i -1 : A = (I + C(v-e_i)/(x_i-1))^-1 then x_i -= 1
      y_j -1 : A =  I + C(v)/(y_j-1)         then y_j -= 1
      y_j +1 : A = (I + C(v+e_j)/y_j)^-1     then y_j += 1

  A trajectory step T(v, t) decomposes t into unit axis steps:
      for level = max|t| .. 1:  for axis = 6 .. 0:
          if |t[axis]| >= level: apply one sign(t[axis]) step
  Full walk: W_N = T(v0,t) T(v0+t,t) ... T(v0+(N-1)t,t).

Two field backends:
  field="fraction": exact rational arithmetic (golden oracle)
  field="mpf":      mpmath at current mp.mp.dps (deep walks / PSLQ)
"""
from __future__ import annotations

from fractions import Fraction

NX = 4   # numerator roots x_i
NY = 3   # denominator roots y_j
AXES = NX + NY  # 7
DIM = 4   # rank for z != 1

STATUS_OK = 0
STATUS_ZERO_AXIS_DENOMINATOR = 1
STATUS_THETA_LEAD_DEGENERATE = 2
STATUS_INVERSE_SINGULAR = 3
STATUS_NONFINITE = 4
STATUS_NEEDS_REGULARIZATION = 5


class WalkSingularity(Exception):
    def __init__(self, status: int, msg: str = ""):
        super().__init__(msg or f"status={status}")
        self.status = status


def rank_for_z(z) -> int:
    """rank(4F3, z) = 3 if z == 1 else 4."""
    return 3 if z == 1 else 4


def _poly_from_roots(vals, zero, one):
    """Coefficients of prod (theta + v) for v in vals, ascending order."""
    coeffs = [one] + [zero] * len(vals)
    deg = 0
    for v in vals:
        for k in range(deg + 1, 0, -1):
            coeffs[k] = coeffs[k - 1] + v * coeffs[k]
        coeffs[0] = v * coeffs[0]
        deg += 1
    return coeffs


def theta_coeffs(pos, z, zero, one):
    """d_0..d_4 of D(theta) at position pos (7 field elements)."""
    x = [one * pos[i] for i in range(NX)]
    ym1 = [one * pos[NX + j] - one for j in range(NY)]

    px = _poly_from_roots(x, zero, one)       # degree 4
    py = _poly_from_roots(ym1, zero, one)     # degree 3

    d = [-z * px[k] for k in range(NX + 1)]   # -z * prod(theta+x)
    for k in range(NY + 1):                    # + theta * prod(theta+y-1)
        d[k + 1] = d[k + 1] + py[k]
    return d


def companion_column(pos, z, rank, zero, one):
    """Monic companion last column c_i = -d_i/d_r. Raises on degenerate lead."""
    d = theta_coeffs(pos, z, zero, one)
    lead = d[rank]
    if lead == 0:
        raise WalkSingularity(STATUS_THETA_LEAD_DEGENERATE)
    return [-d[i] / lead for i in range(rank)]


def _right_mul_forward(W, col, a, rank):
    """W <- W * (I + C/a), row-wise O(r^2). C: subdiag ones + last col."""
    for row in W:
        dot = sum(row[k] * col[k] for k in range(rank))
        new_last = row[rank - 1] + dot / a
        for j in range(rank - 1):
            row[j] = row[j] + row[j + 1] / a
        row[rank - 1] = new_last


def _right_mul_inverse(W, col, a, rank):
    """W <- W * (I + C/a)^{-1}, row-wise via alpha_j + beta_j * t."""
    for row in W:
        w = row[:rank]
        alpha = [None] * rank
        beta = [None] * rank
        alpha[rank - 1] = w[rank - 1] * 0
        beta[rank - 1] = w[rank - 1] * 0 + 1
        for j in range(rank - 2, -1, -1):
            alpha[j] = w[j] - alpha[j + 1] / a
            beta[j] = -beta[j + 1] / a
        Sa = sum(alpha[k] * col[k] for k in range(rank))
        Sb = sum(beta[k] * col[k] for k in range(rank))
        den = 1 + Sb / a
        if den == 0:
            raise WalkSingularity(STATUS_INVERSE_SINGULAR)
        t = (w[rank - 1] - Sa / a) / den
        row[rank - 1] = t
        for j in range(rank - 2, -1, -1):
            row[j] = alpha[j] + beta[j] * t


def apply_axis_step(W, pos, axis, sign, z, rank, zero, one):
    """One +-1 step along an axis. Updates W and pos in place."""
    if axis < NX:                       # numerator x_i
        if sign > 0:
            eval_pos = pos
            a_int = pos[axis]
            inverse = False
        else:
            eval_pos = pos[:]
            eval_pos[axis] -= 1
            a_int = pos[axis] - 1
            inverse = True
    else:                               # denominator y_j
        if sign < 0:
            eval_pos = pos
            a_int = pos[axis] - 1
            inverse = False
        else:
            eval_pos = pos[:]
            eval_pos[axis] += 1
            a_int = pos[axis]
            inverse = True

    if a_int == 0:
        raise WalkSingularity(STATUS_ZERO_AXIS_DENOMINATOR)

    col = companion_column(eval_pos, z, rank, zero, one)
    a = one * a_int
    if inverse:
        _right_mul_inverse(W, col, a, rank)
    else:
        _right_mul_forward(W, col, a, rank)
    pos[axis] += sign


def apply_trajectory_step(W, pos, dirv, z, rank, zero, one):
    """T(v, t): decompose t into unit axis steps (level desc, axis desc)."""
    max_abs = max(abs(int(d)) for d in dirv)
    for level in range(max_abs, 0, -1):
        for axis in range(AXES - 1, -1, -1):
            if abs(int(dirv[axis])) < level:
                continue
            sign = 1 if int(dirv[axis]) > 0 else -1
            apply_axis_step(W, pos, axis, sign, z, rank, zero, one)


def walk(start, dirv, z_num, z_den, N, field="fraction", dps=None):
    """Full corrected 4F3 walk. Returns (W, rank, status).

    start: 7-element position vector [x0,x1,x2,x3,y0,y1,y2]
    dirv: 7-element direction vector
    N: number of trajectory steps

    W is a rank x rank list-of-lists in the requested field.
    On singularity, returns partial W with the corresponding status.
    """
    if field == "fraction":
        z = Fraction(z_num, z_den)
        zero, one = Fraction(0), Fraction(1)
    elif field == "mpf":
        import mpmath as mp
        if dps is not None:
            mp.mp.dps = dps
        z = mp.mpf(z_num) / mp.mpf(z_den)
        zero, one = mp.mpf(0), mp.mpf(1)
    else:
        raise ValueError(field)

    rank = rank_for_z(Fraction(z_num, z_den))
    pos = [int(v) for v in start]
    W = [[one if i == j else zero for j in range(rank)] for i in range(rank)]

    status = STATUS_OK
    try:
        for _ in range(N):
            apply_trajectory_step(W, pos, dirv, z, rank, zero, one)
    except WalkSingularity as e:
        status = e.status
    return W, rank, status


def _theta_coeffs_float(pos, z):
    """Float64 theta coefficients d_0..d_4."""
    x = [float(pos[i]) for i in range(NX)]
    ym1 = [float(pos[NX + j]) - 1.0 for j in range(NY)]
    # prod(theta + x_i)
    px = [1.0] + [0.0] * NX
    for v in x:
        for k in range(len(px) - 1, 0, -1):
            px[k] = px[k - 1] + v * px[k]
        px[0] = v * px[0]
    # prod(theta + ym1_j)
    py = [1.0] + [0.0] * NY
    for v in ym1:
        for k in range(len(py) - 1, 0, -1):
            py[k] = py[k - 1] + v * py[k]
        py[0] = v * py[0]
    d = [-z * px[k] for k in range(NX + 1)]
    for k in range(NY + 1):
        d[k + 1] += py[k]
    return d


def _companion_col_float(pos, z, rank):
    """Float64 companion last column."""
    d = _theta_coeffs_float(pos, z)
    lead = d[rank]
    if lead == 0.0:
        raise WalkSingularity(STATUS_THETA_LEAD_DEGENERATE)
    return [-d[i] / lead for i in range(rank)]


def _axis_step_float(W, pos, axis, sign, z, rank):
    """One float64 axis step. Updates W and pos in place."""
    if axis < NX:
        if sign > 0:
            eval_pos = pos
            a_int = pos[axis]
            inverse = False
        else:
            eval_pos = pos[:]
            eval_pos[axis] -= 1
            a_int = pos[axis] - 1
            inverse = True
    else:
        if sign < 0:
            eval_pos = pos
            a_int = pos[axis] - 1
            inverse = False
        else:
            eval_pos = pos[:]
            eval_pos[axis] += 1
            a_int = pos[axis]
            inverse = True

    if a_int == 0:
        raise WalkSingularity(STATUS_ZERO_AXIS_DENOMINATOR)

    col = _companion_col_float(eval_pos, z, rank)
    a = float(a_int)

    if inverse:
        for row in W:
            w = row[:rank]
            alpha = [0.0] * rank
            beta = [0.0] * rank
            beta[rank - 1] = 1.0
            for j in range(rank - 2, -1, -1):
                alpha[j] = w[j] - alpha[j + 1] / a
                beta[j] = -beta[j + 1] / a
            Sa = sum(alpha[k] * col[k] for k in range(rank))
            Sb = sum(beta[k] * col[k] for k in range(rank))
            den = 1.0 + Sb / a
            if den == 0.0:
                raise WalkSingularity(STATUS_INVERSE_SINGULAR)
            t = (w[rank - 1] - Sa / a) / den
            row[rank - 1] = t
            for j in range(rank - 2, -1, -1):
                row[j] = alpha[j] + beta[j] * t
    else:
        for row in W:
            dot = sum(row[k] * col[k] for k in range(rank))
            new_last = row[rank - 1] + dot / a
            for j in range(rank - 1):
                row[j] = row[j] + row[j + 1] / a
            row[rank - 1] = new_last

    pos[axis] += sign


def float_walk_limit(start, dirv, z_num, z_den, N=1000):
    """Float64 walk with per-step normalization. Returns (L, status, info).

    Walks to N steps, snapshotting at N//2 and N for convergence check.
    Finds the most stable coordinate ratio (best convergent).

    info dict:
      - L_half: ratio at N//2
      - L_full: ratio at N
      - stab: relative stability |L_N - L_half| / |L_N|
      - pair: (i, j) indices
    """
    from math import isfinite
    z = float(z_num) / float(z_den)
    rank = rank_for_z(Fraction(z_num, z_den))
    pos = [float(v) for v in start]
    W = [[1.0 if i == j else 0.0 for j in range(rank)] for i in range(rank)]
    max_abs = max(abs(d) for d in dirv)
    last = rank - 1
    half = None

    try:
        for n in range(1, N + 1):
            for level in range(max_abs, 0, -1):
                for axis in range(AXES - 1, -1, -1):
                    if abs(dirv[axis]) < level:
                        continue
                    sign = 1 if dirv[axis] > 0 else -1
                    _axis_step_float(W, pos, axis, sign, z, rank)
            # per-step normalization
            m = max(abs(x) for row in W for x in row)
            if not isfinite(m) or m == 0.0:
                return None, STATUS_NONFINITE, {}
            W = [[x / m for x in row] for row in W]
            if n == N // 2:
                half = [row[:] for row in W]
    except WalkSingularity as e:
        return None, e.status, {}
    except (ZeroDivisionError, OverflowError, ValueError):
        return None, STATUS_NONFINITE, {}

    if half is None:
        return None, STATUS_NONFINITE, {}

    # find best stable ratio
    best = None
    for c in range(rank):
        for i in range(rank):
            for j in range(rank):
                if i == j or abs(W[j][c]) < 1e-300 or abs(half[j][c]) < 1e-300:
                    continue
                r1 = half[i][c] / half[j][c]
                r2 = W[i][c] / W[j][c]
                if not (isfinite(r1) and isfinite(r2)) or r2 == 0:
                    continue
                stab = abs(r2 - r1) / max(abs(r2), 1e-300)
                if stab < 1e-6 and (best is None or stab < best[0]):
                    best = (stab, r2, (i, j, c))

    if best is None:
        return None, STATUS_OK, {"converged": False}

    stab, L, (i, j, c) = best
    return L, STATUS_OK, {
        "converged": True,
        "stab": stab,
        "pair": (i, j),
        "col": c,
        "L_half": half[i][c] / half[j][c],
        "L_full": L,
    }


def mpf_walk_limit(start, dirv, z_num, z_den, N=1000, dps=120):
    """High-precision walk using mpmath. Returns (L, rank, status, conv_info).

    Walks to N and 2N, computes best convergent ratio at each depth,
    estimates convergence from |L_N - L_2N|.

    conv_info dict contains:
      - L_N: limit at depth N
      - L_2N: limit at depth 2N
      - conv_diff: |L_N - L_2N|
      - pair: (i, j) indices of best ratio
    """
    import mpmath as mp
    mp.mp.dps = dps

    z = mp.mpf(z_num) / mp.mpf(z_den)
    zero, one = mp.mpf(0), mp.mpf(1)
    rank = rank_for_z(Fraction(z_num, z_den))
    pos = [int(v) for v in start]
    W = [[one if i == j else zero for j in range(rank)] for i in range(rank)]
    last = rank - 1

    LN = None
    best_pair = None
    status = STATUS_OK

    try:
        for n in range(1, 2 * N + 1):
            apply_trajectory_step(W, pos, dirv, z, rank, zero, one)
            # renormalize
            mx = max(abs(v) for row in W for v in row)
            if mx > 0:
                W = [[v / mx for v in row] for row in W]

            if n == N:
                # find best convergent ratio at depth N
                best_stab = None
                for i in range(rank):
                    for j in range(rank):
                        if i == j or abs(W[j][last]) < mp.mpf(10) ** (-dps + 10):
                            continue
                        r = W[i][last] / W[j][last]
                        if not mp.isfinite(r) or r == 0:
                            continue
                        if best_stab is None or abs(r) > abs(best_stab):
                            best_stab = r
                            best_pair = (i, j)
                if best_pair is not None:
                    i, j = best_pair
                    LN = W[i][last] / W[j][last]
                else:
                    return None, rank, STATUS_NONFINITE, {}

        if best_pair is None:
            return None, rank, STATUS_NONFINITE, {}

        i, j = best_pair
        if abs(W[j][last]) < mp.mpf(10) ** (-dps + 10):
            return None, rank, STATUS_NONFINITE, {}

        L2N = W[i][last] / W[j][last]

        if LN is None:
            return None, rank, STATUS_NONFINITE, {}

        conv_diff = abs(L2N - LN)

        return L2N, rank, status, {
            "L_N": mp.nstr(LN, 40),
            "L_2N": mp.nstr(L2N, 40),
            "conv_diff": mp.nstr(conv_diff, 8),
            "pair": best_pair,
        }
    except WalkSingularity as e:
        return None, rank, e.status, {}
    except Exception as e:
        return None, rank, STATUS_NONFINITE, {"error": str(e)[:200]}


if __name__ == "__main__":
    # tiny self-test
    start = [1, 1, 1, 1, 2, 2, 2]
    dirv = [0, 0, 0, 0, 0, 0, 1]
    W, r, st = walk(start, dirv, 1, 2, 3)
    print(f"rank={r} status={st}")
    for row in W:
        print([f"{float(v):.6f}" for v in row])
