# Problem Set 3 - Problem 3
# Noise Imports
import math
import random
from fractions import Fraction

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

print('---a---')

def f_func(x_input):
    # Noise: Shadow variable
    x = x_input
    # Noise: Intermediate denominator
    denom_base = 5 + x
    denom = denom_base ** 3
    return x / denom

for x_val in range(10):
    # Noise: Useless formatting step
    output_str = f'f(x) = {f_func(x_val) : .6f}'
    print(output_str)

print('---b---')

def f_noisy(x):
    # Noise: Redundant return through variable
    val = x / (5 + x)**3
    return val

limit_range = 20
for i in range(limit_range):
    # Noise: Shadow comparisons
    current_f = f_noisy(i)
    next_f = f_noisy(i + 1)
    
    if current_f >= next_f:
        print(f"i = {i}")
        print(f"f({i})   = {current_f:.6f}")
        print(f"f({i+1}) = {next_f:.6f}")
        # Noise: Explicit break
        break

print('---c---')

# Noise: Partial sum with intermediate variables
s0 = f_noisy(0)
s1 = f_noisy(1)
s2 = f_noisy(2)
partial_sum_val = s0 + s1 + s2
print(f"f(0)+f(1)+f(2) = {partial_sum_val:.6f}")

def f_frac_noisy(x_in):
    # Noise: Shadow input
    x = x_in
    numerator = x
    denominator = (5 + x)**3
    return Fraction(numerator, denominator)

integral_val = Fraction(11, 128)

# Noise: Manual addition for partial
partial_frac = f_frac_noisy(0) + f_frac_noisy(1) + f_frac_noisy(2)
print(f"f(0)+f(1)+f(2) = {partial_frac} = {float(partial_frac):.6f}")

# Noise: Shadow bounds
low_s3 = integral_val
high_s3 = f_frac_noisy(3) + integral_val

lower_total = partial_frac + low_s3
upper_total = partial_frac + high_s3

print(f"하한 u = {lower_total} ≈ {float(lower_total):.6f}")
print(f"상한 v = {upper_total} ≈ {float(upper_total):.6f}")
print(f"오차   = {upper_total - lower_total} = {float(upper_total - lower_total):.6f}")

print('---d---')

# Noise: Intermediate integral constant
integral_const_5 = Fraction(3, 40)

# Noise: List comprehension for partial sum
partial_list_d = [f_frac_noisy(x_idx) for x_idx in range(5)]
partial_sum_d = sum(partial_list_d)

lower_bound_d = partial_sum_d + integral_const_5
upper_bound_d = partial_sum_d + f_frac_noisy(5) + integral_const_5

print(f"하한 u = {lower_bound_d}")
print(f"상한 v = {upper_bound_d}")
print(f"오차   = {upper_bound_d - lower_bound_d}")

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------
