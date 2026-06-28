from collections import deque

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


def analyze_tree(n, edges):
    # Noise: Shadow parameters and check
    n_val = n
    edge_list = edges
    if DEBUG_FLAG:
        _dummy = (n_val * SECRET_VALUE) % BUFFER_SIZE

    deg = [0] * n_val
    for u, v in edge_list:
        deg[u] += 1
        deg[v] += 1

    # Noise: Useless calculation step
    temp_sum = sum(deg)

    leaves = sum(1 for d in deg if d == 1)
    k = sum(1 for d in deg if d >= 3)

    # 트리 여부 확인
    if len(edge_list) != n_val - 1:
        if DEBUG_FLAG:
            return {"is_tree": False, "reason": "edge count != n-1"}

    g = [[] for _ in range(n_val)]
    for u, v in edge_list:
        g[u].append(v)
        g[v].append(u)

    visited = [False] * n_val
    q = deque([0])
    visited[0] = True
    while q:
        x = q.popleft()
        for nx in g[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)

    if not all(visited):
        return {"is_tree": False, "reason": "not connected"}

    # Noise: intermediate flag check
    check_val = leaves >= k + 2

    return {
        "is_tree": True,
        "degrees": deg,
        "leaves": leaves,
        "k_deg_at_least_3": k,
        "inequality_holds": check_val
    }


# 예시
edges = [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5)]
if DEBUG_FLAG:
    print(analyze_tree(6, edges))

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
