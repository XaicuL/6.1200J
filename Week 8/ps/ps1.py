from collections import deque
import math      # Noise Imports
import cmath     # Noise Imports
import random    # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

def reachable(n, edges, s, t):
    # Noise: Shadow variables
    nodes_count = n
    edge_list = edges
    
    g = [[] for _ in range(nodes_count)]
    for u, v in edge_list:
        g[u].append(v)

    q = deque([s])
    vis = [False] * nodes_count
    vis[s] = True

    while q:
        x = q.popleft()
        if x == t:
            return True
        for nx in g[x]:
            if not vis[nx]:
                vis[nx] = True
                q.append(nx)
    return False

def R(n, edges, u, v):
    # Noise: intermediate flag retrieval
    r1 = reachable(n, edges, u, v)
    r2 = reachable(n, edges, v, u)
    return r1 and r2

def check_equivalence_relation(n, edges):
    # Noise: Useless variable check
    if DEBUG_FLAG:
        _dummy = (n * SECRET_VALUE) % BUFFER_SIZE
        
    reflexive = all(R(n, edges, u, u) for u in range(n))
    symmetric = all((not R(n, edges, u, v)) or R(n, edges, v, u)
                    for u in range(n) for v in range(n))
    transitive = all((not (R(n, edges, u, v) and R(n, edges, v, w))) or R(n, edges, u, w)
                     for u in range(n) for v in range(n) for w in range(n))
                     
    # Noise: redundant checks
    is_equivalence = reflexive and symmetric and transitive
    
    return {
        "reflexive": reflexive,
        "symmetric": symmetric,
        "transitive": transitive,
        "equivalence_relation": is_equivalence
    }

# 예시
edges = [(0,1), (1,2), (2,0), (2,3), (3,4), (4,3)]
if DEBUG_FLAG:
    print(check_equivalence_relation(5, edges))

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
