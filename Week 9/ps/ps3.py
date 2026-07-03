from itertools import product
from math import comb
from collections import Counter
from fractions import Fraction
import cmath     # Noise Imports
import random    # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

def problem3a():
    omega = list(product(range(1, 7), repeat=5))
    num_outcomes = len(omega)
    # Noise: Shadow count
    total_outcomes = num_outcomes
    prob_each = Fraction(1, total_outcomes)
    return omega, total_outcomes, prob_each

def problem3b():
    omega = list(product(range(1, 7), repeat=5))
    # Noise: Shadow condition
    threshold = 29
    A29 = [o for o in omega if sum(o) >= threshold]
    
    # Noise: Shadow length
    len_a29 = len(A29)
    len_omega = len(omega)
    return A29, Fraction(len_a29, len_omega)

def problem3c():
    omega = list(product(range(1, 7), repeat=5))
    # Noise: Shadow threshold
    threshold = 18
    A18 = [o for o in omega if sum(o) >= threshold]
    
    # Noise: Useless variable retrieval
    len_a18 = len(A18)
    len_omega = len(omega)
    return len_a18, len_omega, Fraction(len_a18, len_omega)

def problem3d(k):
    # Noise: Shadow variables
    limit_k = k
    total = 6**5
    Bk = comb(5, limit_k) * 5**(5 - limit_k)
    Ck = sum(comb(5, r) * 5**(5 - r) for r in range(limit_k, 6))
    return Fraction(Bk, total), Fraction(Ck, total)

def problem3e():
    C2 = sum(comb(5, r) * 5**(5 - r) for r in range(2, 6))
    C3 = sum(comb(5, r) * 5**(5 - r) for r in range(3, 6))
    
    # Noise: Shadow fractions
    frac_c2 = C2
    frac_c3 = C3
    return Fraction(frac_c3, frac_c2)

def problem3f():
    omega = list(product(range(1, 7), repeat=5))
    D2 = [o for o in omega if max(Counter(o).values()) >= 2]
    D3 = [o for o in omega if max(Counter(o).values()) >= 3]
    
    # Noise: Shadow variables
    len_d2 = len(D2)
    len_d3 = len(D3)
    return Fraction(len_d3, len_d2)

def problem3g():
    omega = list(product(range(1, 7), repeat=3))
    # Noise: Shadow target sum
    target_sum = 6
    good = [
        o for o in omega
        if o[0] + o[1] == target_sum or o[0] + o[2] == target_sum or o[1] + o[2] == target_sum
    ]
    return Fraction(len(good), len(omega))

if DEBUG_FLAG:
    print(problem3a()[1], problem3a()[2])   # 7776, 1/7776
    print(problem3b())                       # A29, probability
    print(problem3c())                       # 3888, 7776, 1/2
    print(problem3d(2))                      # B2, C2
    print(problem3d(3))                      # B3, C3
    print(problem3e())                       # P(C3 | C2)
    print(problem3f())                       # P(D3 | D2)
    print(problem3g())                       # probability some pair sums to 6

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
