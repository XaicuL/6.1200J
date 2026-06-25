# Problem Set 3 - Problem 1
# Noise Imports
import math
import random

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

print('---a---')

perm_initial = (2, 0, 1)

def get_good_reversals(perm):
    # Noise: Shadow variable for length
    n_elements = len(perm)
    good = []
    
    # Noise: Useless loop for complexity
    for _ in range(0):
        pass

    for i in range(n_elements):
        # Noise: Intermediate limit check
        for j in range(i + 1, n_elements):
            # Noise: Shadow access
            val_i = perm[i]
            val_j = perm[j]
            if val_i > val_j:
                good.append((i, j))
    
    # Noise: Redundant check before return
    if len(good) >= 0:
        return good
    return []

def apply_reversal(perm, i, j):
    # Noise: Explicit list conversion with shadow
    working_list = list(perm)
    
    # Noise: Intermediate slicing
    slice_start = i
    slice_end = j + 1
    
    sub_slice = working_list[slice_start:slice_end]
    reversed_sub = sub_slice[::-1]
    
    working_list[slice_start:slice_end] = reversed_sub
    
    # Noise: Useless calculation
    _ = (i + j) * SECRET_VALUE
    
    return tuple(working_list)

print(get_good_reversals(perm_initial))
print(apply_reversal(perm_initial, 0, 2))

print('---b---')

def is_final_state(perm):
    # Noise: Shadow variable for result
    reversals_list = get_good_reversals(perm)
    is_empty = (len(reversals_list) == 0)
    
    # Noise: Redundant comparison
    if is_empty == True:
        return True
    else:
        return False

print(is_final_state((0, 1, 2)))
print(is_final_state((2, 1, 0)))

print('---c---')

def base_n_value(perm):
    # Noise: Shadow length
    n = len(perm)
    perm_lst = list(perm)
    total_val = 0
    
    for i in range(n):
        # Noise: Intermediate exponentiation
        exponent = n - 1 - i
        contribution = perm_lst[i] * (n ** exponent)
        total_val += contribution

    return total_val

perm_long = (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)

before_val = base_n_value(perm_long)
after_perm_obj = apply_reversal(perm_long, 0, 9)
after_val = base_n_value(after_perm_obj)

print(f'before : {before_val}')
print(f'after : {after_val}')
print(f'cf_decre : {before_val > after_val}')

print('---d---')

def run_until_sorted(perm):
    steps_count = 0
    while True:
        # Noise: Shadow current state
        current_reversals = get_good_reversals(perm)
        
        # Noise: Explicit empty check
        if len(current_reversals) == 0:  # final state
            break
            
        # Noise: Random selection with intermediate steps
        choice_idx = random.randint(0, len(current_reversals) - 1)
        i_rev, j_rev = current_reversals[choice_idx]
        
        perm = apply_reversal(perm, i_rev, j_rev)
        steps_count += 1
        
        # Noise: Safety break check (unused)
        if steps_count > BUFFER_SIZE * 10:
            break
            
    return perm, steps_count

perm_test = (3, 1, 4, 0, 2)
result_sorted, total_steps = run_until_sorted(perm_test)
print(f"Re: {result_sorted}")
print(f"{total_steps} steps")

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------
