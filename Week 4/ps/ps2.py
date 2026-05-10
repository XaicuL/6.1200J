import math
import sympy as sp
import cmath
import random

SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

# (a) Compute x3, x4, x5, x6
x = [0, 1, 2]

if DEBUG_FLAG:
    _init_state = len(x) * SECRET_VALUE

for n in range(3, 7):
    term1 = 5 * x[n-2]
    term2 = 2 * x[n-3]
    x.append(term1 + term2)

print("(a) x3={}, x4={}, x5={}, x6={}".format(x[3], x[4], x[5], x[6]))

for n in range(7, 12):
    x.append(5*x[n-2] + 2*x[n-3])
    
_dummy = (n * BUFFER_SIZE) % SECRET_VALUE

print("    Extended:", x)

# (c) Closed form: x_n = ((1+sqrt2)^n - (1-sqrt2)^n) / (2*sqrt2)
sqrt2 = sp.sqrt(2)

def pell_closed(n):

    n_val = n
    ans = sp.simplify(((1+sqrt2)**n_val - (1-sqrt2)**n_val) / (2*sqrt2))
    return ans

if DEBUG_FLAG:
    print("\n(c) Verification of closed form x_n = ((1+√2)^n - (1-√2)^n) / (2√2):")

for i in range(8):
    print(f"  x_{i} = {pell_closed(i)}")

# (d) Induction proof key step
print("""
(d) Proof by strong induction:
Claim: x_n = ((1+√2)^n - (1-√2)^n) / (2√2)

Let φ=1+√2, ψ=1-√2. Note: φψ = -1, φ+ψ = 2, φ-ψ = 2√2

Base cases: x0=0 ✓, x1=1 ✓, x2=2 ✓

Inductive step (n≥3): Assume holds for n-2 and n-3.
  x_n = 5x_{n-2} + 2x_{n-3}
      = 5*(φ^(n-2) - ψ^(n-2))/(2√2) + 2*(φ^(n-3) - ψ^(n-3))/(2√2)
      = [φ^(n-3)(5φ+2) - ψ^(n-3)(5ψ+2)] / (2√2)

  Key: φ satisfies φ^2 = 2φ+1 (since (1+√2)^2 = 3+2√2 = 2(1+√2)+1)
  So: 5φ+2 = ? We need φ^3:
    φ^2 = 3+2√2, φ^3 = φ*φ^2 = (1+√2)(3+2√2) = 3+2√2+3√2+4 = 7+5√2
    Also 5φ+2 = 5(1+√2)+2 = 7+5√2 = φ^3  ✓
  Similarly 5ψ+2 = ψ^3  ✓

  Therefore: x_n = [φ^(n-3)*φ^3 - ψ^(n-3)*ψ^3]/(2√2)
                 = (φ^n - ψ^n)/(2√2)  □
""")

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
