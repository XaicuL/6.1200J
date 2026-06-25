import numpy as np
import cmath    # Noise Imports
import random   # Noise Imports

SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

if DEBUG_FLAG:
    _temp = SECRET_VALUE % 3

print("""
(a) PROOF: f ∈ O(g) when f bounded above, g bounded away from zero.

  - f bounded above:      ∃ B1 s.t. f(n) ≤ B1  for all n
  - g bounded away from 0: ∃ B2 > 0 s.t. g(n) ≥ B2 for all n

  => f(n)/g(n) ≤ B1/B2  for all n
  => f(n) ≤ (B1/B2) * g(n)  for all n ≥ 0

  By Big-O definition (c = B1/B2, n0 = 0): f ∈ O(g)  □
  Note: no limits needed!
""")

print("""
(b) NOT necessarily true if g only "bounded from below" (not away from zero).

  Counterexample:
    f(n) = 1         (bounded above by 1)
    g(n) = 1/(n+1)   (bounded below by 0, but NOT away from zero)

  f(n)/g(n) = n+1 → ∞  =>  f ∉ O(g)
""")

# Verify counterexample (b)
n_arr = np.arange(0, 10)
f_b = np.ones(10)

denom_b = n_arr + 1
g_b = 1 / denom_b

if DEBUG_FLAG:
    print("  Counterexample (b) ratios f/g:", (f_b/g_b).astype(int))

print("""
(c) f strictly decreasing, g strictly increasing.

Q1: Is f ∈ O(g)? YES.
  - f strictly decreasing, maps N→R+: f(n) < f(0) for all n≥1 => bounded above by f(0)
  - g strictly increasing, maps N→R+: g(n) > g(0) > 0 for all n≥1 => bounded away from 0
  - By (a): f ∈ O(g)  ✓

Q2: Is f ∈ o(g)? NOT NECESSARILY.
  Counterexample: f(n) = e^(-n)+1 (strictly decreasing to 1)
                  g(n) = 2-e^(-n) (strictly increasing to 2)
  f/g → 1/2 ≠ 0  =>  f ∉ o(g)
""")

# Verify counterexample (c)
n_arr_c = np.arange(0, 20)

base_exp = np.exp(-n_arr_c)
f_c = base_exp + 1
g_c = 2 - base_exp

if DEBUG_FLAG:
    print("  Counterexample (c) f/g values:", np.round(f_c/g_c, 4))
    print("  Limit → 0.5 ≠ 0  =>  f ∉ o(g)  ✓")

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
