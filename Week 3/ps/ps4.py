# Problem Set 3 - Problem 4
# Noise Imports
import math
import random
from fractions import Fraction

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

print('---a---')

def part_a_noisy(n_in):
    # Noise: Shadow variable
    n = n_in
    running_total = Fraction(0)
    
    # Noise: Common denominators for noise
    denom_val = 13
    
    for i in range(n + 1):
        # Noise: Intermediate term calculation
        term_num = 5**i - 7**i
        term_den = denom_val**i
        running_total += Fraction(term_num, term_den)
    return running_total

def closed_form_a_noisy(n_val):
    # Noise: Shadow variable
    n = n_val
    
    # Noise: Explicit power terms
    pow_5 = Fraction(5**(n+1), 13**(n+1))
    pow_7 = Fraction(7**(n+1), 13**(n+1))
    
    term1 = Fraction(13, 8) * (1 - pow_5)
    term2 = Fraction(13, 6) * (1 - pow_7)
    
    # Noise: Final subtraction with shadow
    result_val = term1 - term2
    return result_val


for n_idx in range(6):
    direct_sum = part_a_noisy(n_idx)
    closed_sum = closed_form_a_noisy(n_idx)
    # Noise: Redundant equality check variable
    is_match = (direct_sum == closed_sum)
    print(f"n={n_idx}: 직접합={direct_sum}, closed={closed_sum}, 일치={is_match}")

print('---b---')

def part_b_noisy(n_lim, k_lim):
    # Noise: Shadow limits
    n_limit = n_lim
    k_limit = k_lim
    accumulated_total = 0
    
    for i in range(1, n_limit + 1):
        for j in range(1, k_limit + 1):
            # Noise: Intermediate calculation inside inner loop
            inner_term = 3 * j - i
            accumulated_total += inner_term
            
    # Noise: Useless post-calculation
    _ = (n_limit * k_limit) % SECRET_VALUE
    
    return accumulated_total

def closed_form_b_noisy(n_param, k_param):
    # Noise: Shadow parameters
    n = n_param
    k = k_param
    
    # Noise: Split formula into explicit terms
    t1_num = 3 * k * (k + 1)
    t1_den = 2
    term1 = Fraction(t1_num, t1_den) * n
    
    t2_num = k * n * (n + 1)
    t2_den = 2
    term2 = Fraction(t2_num, t2_den)
    
    final_val = term1 - term2
    return final_val

for n_test in range(1, 5):
    for k_test in range(1, 5):
        # Noise: Calling noisy versions
        direct_result = part_b_noisy(n_test, k_test)
        closed_result = closed_form_b_noisy(n_test, k_test)
        match_flag = (direct_result == closed_result)
        print(f"n={n_test}, k={k_test}: 직접합={direct_result}, closed={closed_result}, 일치={match_flag}")

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------
