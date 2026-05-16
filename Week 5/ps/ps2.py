# Problem 2. Computing Modular Inverses
# MIT 6.1200J Problem Set 5
#
# Goal: find 15^{-1} mod 43, i.e. some x in [0, 43) with 15x ≡ 1 (mod 43).


# ── Part (a): Pulverizer ───────────────────────────────────────────────────────
#
# We run the extended Euclidean algorithm on (43, 15), maintaining
# coefficients s, t such that 43*s + 15*t = current remainder.
#
# Step-by-step:
#
#   43 = 2*15 + 13    →  13 = 1*43 + (-2)*15
#   15 = 1*13 +  2    →   2 = (-1)*43 + 3*15     [subst: 13 = 43 - 2*15]
#   13 = 6* 2 +  1    →   1 = 7*43 + (-20)*15    [subst: 2 = -43 + 3*15]
#    2 = 2* 1 +  0    →  done, gcd = 1
#
# So  7*43 + (-20)*15 = 1,  meaning  15*(-20) ≡ 1 (mod 43).
# Since -20 mod 43 = 23,  the answer is 15^{-1} ≡ 23 (mod 43).

print("Part (a) — Pulverizer")
print()

# Reproduce the table by hand to show work:
steps = [
    # (x,   y,   s_x, t_x,  s_y, t_y,  q,   r)
    #  sa + tb = x,  ua + vb = y
]

a_val, b_val = 43, 15
x, y = a_val, b_val
sx, tx = 1, 0   # 1*43 + 0*15 = 43
sy, ty = 0, 1   # 0*43 + 1*15 = 15

print(f"  {'x':>5}  {'y':>5}  {'s':>5}  {'t':>5}   equation")
print(f"  {'─'*5}  {'─'*5}  {'─'*5}  {'─'*5}   {'─'*20}")
print(f"  {x:>5}  {y:>5}  {sx:>5}  {tx:>5}   {sx}*43 + ({tx})*15 = {x}")
while y > 0:
    q, r = x // y, x % y
    x,  y  = y,  r
    sx, sy = sy, sx - q*sy
    tx, ty = ty, tx - q*ty
    print(f"  {x:>5}  {y:>5}  {sx:>5}  {tx:>5}   ({sx})*43 + ({tx})*15 = {x}")

inv_pulv = tx % b_val   # t is the coefficient of 15 once gcd is reached
# wait — at termination x=gcd, and sx*43 + tx*15 = gcd.
# But the loop overwrites; let's redo cleanly:

def pulverizer(a, b):
    x, y, s, t, u, v = a, b, 1, 0, 0, 1
    while y:
        q, r = x // y, x % y
        x, y, s, t, u, v = y, r, u, v, s - q*u, t - q*v
    return x, s, t   # gcd, coeff of a, coeff of b

gcd_val, coeff_a, coeff_b = pulverizer(43, 15)
inv_a = coeff_b % 43

print()
print(f"  Result:  ({coeff_a})*43 + ({coeff_b})*15 = {gcd_val}")
print(f"  15^{{-1}} = {coeff_b} mod 43 = {inv_a}")
print(f"  Check:   15 * {inv_a} mod 43 = {15 * inv_a % 43}  ✓")


# ── Part (b): Fermat's Little Theorem ─────────────────────────────────────────
#
# Since 43 is prime and gcd(15, 43) = 1, Fermat's Little Theorem gives:
#     15^{42} ≡ 1  (mod 43)
#
# Multiplying both sides by 15^{-1}:
#     15^{-1} ≡ 15^{41}  (mod 43)
#
# We compute 15^{41} mod 43 by repeated squaring.
# 41 in binary = 32 + 8 + 1 = 101001_2, so we need powers 1, 8, 32.
#
#   15^1  = 15
#   15^2  = 225        = 5*43 + 10   → 10  (mod 43)
#   15^4  = 10^2 = 100 = 2*43 + 14  → 14
#   15^8  = 14^2 = 196 = 4*43 + 24  → 24
#   15^16 = 24^2 = 576 = 13*43 + 17 → 17
#   15^32 = 17^2 = 289 = 6*43 + 31  → 31
#
#   15^41 = 15^32 * 15^8 * 15^1
#         = 31 * 24 * 15  (mod 43)
#         = 744 * 15      (mod 43)      [31*24 = 744 = 17*43 + 13 → 13]
#         = 13 * 15 = 195 = 4*43 + 23  → 23  (mod 43)
#
# So 15^{-1} ≡ 23  (mod 43).

print()
print("Part (b) — Fermat's Little Theorem")
print()
print("  Repeated squaring of 15 mod 43:")
val, mod = 15, 43
power = val
table = {1: power}
for exp in [2, 4, 8, 16, 32]:
    power = (power * power) % mod
    table[exp] = power
    print(f"  15^{exp:<3} = {power:>3}  (mod 43)")

result = (table[32] * table[8] * table[1]) % mod
print()
print(f"  15^41 = 15^32 * 15^8 * 15^1")
print(f"        = {table[32]} * {table[8]} * {table[1]}  (mod 43)")
print(f"        = {result}")
print(f"  Check: 15 * {result} mod 43 = {15 * result % 43}  ✓")
print()
print(f"  Both methods agree: 15^{{-1}} mod 43 = 23")
