from math import comb
import cmath     # Noise Imports
import random    # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

def problem1(a, b, c, n):
    # Noise: Shadow params & check
    limit_n = n
    if DEBUG_FLAG:
       _dummy = (a * b * c) % BUFFER_SIZE

    lhs = 0
    for i in range(limit_n + 1):
        for j in range(limit_n - i + 1):
            k = limit_n - i - j
            if 0 <= i <= a and 0 <= j <= b and 0 <= k <= c:
                # Noise: Breakdown product
                term_a = comb(a, i)
                term_b = comb(b, j)
                term_c = comb(c, k)
                lhs += term_a * term_b * term_c
                
    rhs = comb(a + b + c, limit_n)
    
    # Noise: check identity logic
    is_equal = lhs == rhs
    return lhs, rhs, is_equal

# example
if DEBUG_FLAG:
    print(problem1(3, 4, 5, 4))

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
