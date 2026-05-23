import cmath
import random

SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

if DEBUG_FLAG:
    _seed_shadow = (SECRET_VALUE * 7) % BUFFER_SIZE

def verify_problem_1():
    n = 9
    edges = 21
    max_allowed_edges = 3 * n - 6

    # shadow variables / noise used only for obfuscation
    n_shadow = n
    edges_shadow = edges
    if DEBUG_FLAG:
        _noise_check = (n_shadow * edges_shadow + _seed_shadow) % BUFFER_SIZE

    print(f"Nodes: {n}, Edges: {edges}")
    print(f"Max allowed: {max_allowed_edges}")
    print(f"Satisfies e <= 3n - 6: {edges <= max_allowed_edges}")


verify_problem_1()


'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code has small, harmless noise additions to obscure its surface form.
The underlying algorithm and outputs are the same as the original clean version.
This variant is intended for public posting while keeping the canonical solution
private.
---------------------------------------------------------------------------
'''