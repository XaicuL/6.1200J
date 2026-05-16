# Problem 1. Fibonacci Divisibility
# MIT 6.1200J Problem Set 5

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ── Part (a) ──────────────────────────────────────────────────────────────────
# Claim: F_{n+a} ≡ F_n * F_{a+1}  (mod F_a)  for all n ≥ 0.
#
# Proof by strong induction on n (with a > 0 fixed throughout).
#
# Base cases:
#   n = 0: F_{0+a} = F_a ≡ 0 (mod F_a), and F_0 * F_{a+1} = 0 * F_{a+1} = 0. ✓
#   n = 1: F_{1+a} = F_{a+1}, and F_1 * F_{a+1} = 1 * F_{a+1} = F_{a+1}. ✓
#
# Inductive step (n ≥ 2):
#   Assume the claim holds for n-1 and n-2 (strong IH).
#   Then:
#     F_{n+a} = F_{(n-1)+a} + F_{(n-2)+a}          (Fibonacci recurrence)
#             ≡ F_{n-1}*F_{a+1} + F_{n-2}*F_{a+1}  (mod F_a, by IH)
#             = (F_{n-1} + F_{n-2}) * F_{a+1}
#             = F_n * F_{a+1}                        □

print("Part (a) — numerical check: F_{n+a} mod F_a == (F_n * F_{a+1}) mod F_a")
print(f"{'a':>3} {'n':>3}  {'LHS':>8}  {'RHS':>8}  ok?")
print("-" * 32)
for a in range(1, 7):
    fa, fa1 = fib(a), fib(a + 1)
    for n in range(7):
        lhs = fib(n + a) % fa
        rhs = (fib(n) * fa1) % fa
        print(f"{a:>3} {n:>3}  {lhs:>8}  {rhs:>8}  {'✓' if lhs == rhs else '✗'}")
    print()


# ── Part (b) ──────────────────────────────────────────────────────────────────
# Claim: If a | b (i.e. b = k*a for some k ∈ ℕ), then F_a | F_b.
#
# Proof by induction on k (with a > 0 fixed, b = k*a).
#
# Base case (k = 0):
#   b = 0, so F_b = F_0 = 0.  F_a | 0 trivially. ✓
#
# Inductive step:
#   Assume F_a | F_{k*a} for some k ≥ 0.
#   We want to show F_a | F_{(k+1)*a}.
#
#   Apply part (a) with n = k*a:
#       F_{k*a + a} ≡ F_{k*a} * F_{a+1}  (mod F_a).
#
#   By the inductive hypothesis F_a | F_{k*a}, so F_{k*a} ≡ 0 (mod F_a).
#   Therefore F_{(k+1)*a} ≡ 0 * F_{a+1} = 0  (mod F_a),
#   which means F_a | F_{(k+1)*a}.  □

print("Part (b) — numerical check: F_a | F_{k*a}")
print(f"{'a':>3} {'k':>3} {'b':>4}  {'F_a':>6}  {'F_b':>10}  {'F_b % F_a':>10}  ok?")
print("-" * 48)
for a in range(1, 7):
    fa = fib(a)
    for k in range(1, 7):
        b  = k * a
        fb = fib(b)
        r  = fb % fa if fa else 0
        print(f"{a:>3} {k:>3} {b:>4}  {fa:>6}  {fb:>10}  {r:>10}  {'✓' if r == 0 else '✗'}")
    print()
