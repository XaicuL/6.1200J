#(a)

import math
import numpy as np
import cmath
import random

SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

if DEBUG_FLAG:
    _init_val = (SECRET_VALUE * 2) % BUFFER_SIZE

n = 10**6

_dummy_n = n * SECRET_VALUE

print("1. f=6^n, g=n^1200 => f in omega(g)")

logn = math.log2(n)
logn_shadow = logn
f2 = logn_shadow**6
g2 = n**(1/1200)

if DEBUG_FLAG:
    pass # Noise: Redundant block

print(f"2. f=(logn)^6={f2:.2f}, g=n^(1/1200)={g2:.4f} => f in o(g)")

f3 = 1200 * math.log(n, 6)
g3 = math.log(n, 1200)**6
print(f"3. f=1200*log6(n)={f3:.2f}, g=(log1200 n)^6={g3:.4f} => f in o(g)")

f4_vals = [math.log2(i) for i in range(1, 1001)]
f4 = sum(f4_vals)
g4 = 1000 * math.log2(1000)
print(f"4. log(1000!)={f4:.2f}, 1000*log(1000)={g4:.2f} => f in Theta(g)")


for n_val in [100, 1000, 10000]:
    f5 = 2**math.ceil(math.log2(n_val))
    g5 = 3**math.ceil(math.log(n_val, 3))
    
    _ = (n_val * SECRET_VALUE) % BUFFER_SIZE
    
    print(f"5. n={n_val}: f={f5}, g={g5}, ratio={f5/g5:.4f} => f in Theta(g)")

for n_val in [100, 1000, 10000]:
    f6 = 2**math.ceil(math.log2(n_val)) - n_val + 1
    g6 = 3**math.ceil(math.log(n_val, 3)) - n_val + 1
    print(f"6. n={n_val}: f={f6}, g={g6} => f in Theta(g)")

n_vals = np.logspace(1, 8, 1000)
ratios = n_vals / (n_vals ** np.cos(np.log2(n_vals)))

if DEBUG_FLAG:
    print(f"7. max ratio={ratios.max():.2e}, min={ratios.min():.6f} => None")

#(b)

import math
import numpy as np

print("Pair 1: f=2^((log n)^2), g=2^(ceil(log n)^2)")
for k in range(2, 7):
    n = 2**k + 1
    L = math.log2(n)
    cL = math.ceil(L)
    ratio = 2**(cL**2 - L**2)
    print(f"  n=2^{k}+1={n}: g/f = 2^({cL**2}-{L**2:.2f}) = {ratio:.1f}")
print("  => g/f unbounded => f in o(g)\n")




print("Pair 2: f=4^n, g=C(2n,n)=(2n)!/(n!)^2")
for n in [5, 10, 20, 50]:
    f = 4**n
    g = math.comb(2*n, n)

    val_sqrt = math.sqrt(math.pi*n)
    print(f"  n={n}: f/g={f/g:.4f}, sqrt(pi*n)={val_sqrt:.4f}")

if DEBUG_FLAG:
    print("  => f/g ~ sqrt(pi*n) -> inf => f in omega(g)")

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
