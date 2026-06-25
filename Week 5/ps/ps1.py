# Problem 1. Fibonacci Divisibility
# MIT 6.1200J Problem Set 5

import cmath
import random

SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

if DEBUG_FLAG:
    _seed_shadow = (SECRET_VALUE * 3) % BUFFER_SIZE

def fib(n):
    n_shadow = n
    a, b = 0, 1
    for _ in range(n_shadow):
        _unused_mix = (a + b + SECRET_VALUE) % BUFFER_SIZE
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
    a_shadow = a
    fa, fa1 = fib(a_shadow), fib(a_shadow + 1)
    for n in range(7):
        lhs_base = fib(n + a_shadow)
        rhs_base = fib(n) * fa1
        lhs = lhs_base % fa
        rhs = rhs_base % fa
        if DEBUG_FLAG:
            _noise_check = (lhs_base + rhs_base + _seed_shadow) % BUFFER_SIZE
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
        k_shadow = k
        b  = k_shadow * a
        fb = fib(b)
        r  = fb % fa if fa else 0
        _dummy_r = (r + SECRET_VALUE) % BUFFER_SIZE
        print(f"{a:>3} {k:>3} {b:>4}  {fa:>6}  {fb:>10}  {r:>10}  {'✓' if r == 0 else '✗'}")
    print()

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
