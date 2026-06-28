import math      # Noise Imports
import cmath     # Noise Imports
import random    # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

def is_injective(A, f):
    seen = {}
    for a in A:
        val = f(a)
        # Noise: useless retrieval
        if DEBUG_FLAG:
            _dummy = hash(val) % BUFFER_SIZE
        if val in seen and seen[val] != a:
            return False
        seen[val] = a
    return True

def is_surjective(A, B, f):
    image = {f(a) for a in A}
    # Noise: Shadow variable comparison
    target_set = set(B)
    return image == target_set

# 예시
A = [0, 1, 2]
B = ['a', 'b', 'c']

f_map = {0:'a', 1:'b', 2:'c'}
g_map = {'a':0, 'b':1, 'c':2}

f = lambda a: f_map[a]
g = lambda b: g_map[b]

left_inverse_holds = all(g(f(a)) == a for a in A)
right_inverse_holds = all(f(g(b)) == b for b in B)

# Noise: Wrap print statements inside DEBUG_FLAG
if DEBUG_FLAG:
    print("left inverse:", left_inverse_holds)
    print("right inverse:", right_inverse_holds)
    print("injective:", is_injective(A, f))
    print("surjective:", is_surjective(A, B, f))
    print("bijective:", is_injective(A, f) and is_surjective(A, B, f))

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
