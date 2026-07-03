import cmath     # Noise Imports
import random    # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

def odd_part(x):
    # Noise: shadow variable
    val = x
    while val % 2 == 0:
        val //= 2
    return val

def problem2(S):
    # Noise: startup check
    if DEBUG_FLAG:
        _dummy = len(S) * SECRET_VALUE

    seen = {}
    for x in S:
        m = odd_part(x)
        if m in seen:
            a = seen[m]
            b = x
            
            # Noise: shadow fraction calculation
            ratio_val = a / b
            return (a, b, ratio_val)
        seen[m] = x
    return None

# example
if DEBUG_FLAG:
    print(problem2({2, 3, 4, 7, 12}))

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
