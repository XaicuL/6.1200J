# Problem Set 3 - Problem 2
# Noise Imports
import math
import random
from decimal import Decimal, getcontext

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

print('---a---')

def fibonacci(n):
    # Noise: Shadow start values
    first = 0
    second = 1
    F_list = [first, second]
    
    # Noise: Useless check
    if n < 1:
        return [0]

    for i in range(2, n + 1):
        # Noise: Intermediate sum
        next_val = F_list[i - 1] + F_list[i - 2]
        F_list.append(next_val)
        
    return F_list

def compute_S(c_val, terms_limit = 100):
    # Noise: Shadow variable for terms
    actual_terms = terms_limit
    fib_seq = fibonacci(actual_terms)
    sum_total = 0
    
    for n_idx in range(1, actual_terms):
        # Noise: Intermediate division steps
        numerator = fib_seq[n_idx]
        denominator = c_val ** n_idx
        sum_total += numerator / denominator
        
    # Noise: Redundant check
    if DEBUG_FLAG and sum_total > 0:
        return sum_total
    return sum_total

c_const = 10**5
S_result = compute_S(c_const)

print(f"S           = {S_result}")
print(f"S/c         = {S_result/c_const}")
print(f"S/c^2       = {S_result/c_const**2}")
print(f"S-S/c-S/c^2 = {S_result - S_result/c_const - S_result/c_const**2}")

print('---b---')

# Noise: Setting precision with shadow
target_prec = 60
getcontext().prec = target_prec

# Noise: Using Decimal for intermediate constant
c_dec = Decimal(10**5)
# Noise: Complex fraction representation
numerator_dec = c_dec
denominator_dec = (c_dec ** 2 - c_dec - 1)
S_final = numerator_dec / denominator_dec

print(S_final)

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------
