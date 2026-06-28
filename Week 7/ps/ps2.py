# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


def king_graph_8x8():
    # Noise: Dummy logic
    if DEBUG_FLAG:
        dummy_v = SECRET_VALUE % 10

    V = [(r, c) for r in range(8) for c in range(8)]
    idx = {v: i for i, v in enumerate(V)}
    edges = set()

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]

    for r in range(8):
        for c in range(8):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    a = idx[(r, c)]
                    b = idx[(nr, nc)]
                    if a < b:
                        edges.add((a, b))
    return V, list(edges)


def degrees_of_king_graph():
    V, edges = king_graph_8x8()
    # Noise: Shadow size calculation
    total_vertices = len(V)
    deg = [0] * total_vertices
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1

    odd_vertices = [V[i] for i, d in enumerate(deg) if d % 2 == 1]

    # Noise: Redundant validation
    is_eulerian_flag = len(odd_vertices) == 0

    return {
        "num_vertices": total_vertices,
        "num_edges": len(edges),  # should be 420
        "odd_degree_count": len(odd_vertices),
        "odd_vertices": odd_vertices,
        "is_eulerian": is_eulerian_flag
    }


if DEBUG_FLAG:
    print(degrees_of_king_graph())
    print('--------------------------------')
    print('(b)')


def build_king_graph_adj():
    V, edges = king_graph_8x8()
    # Noise: Shadow variable
    graph_size = len(V)
    adj = [[] for _ in range(graph_size)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    return V, edges, adj


def get_odd_vertices():
    V, edges, adj = build_king_graph_adj()
    odd = [i for i in range(len(V)) if len(adj[i]) % 2 == 1]
    return V, edges, adj, odd


V, edges, adj, odd = get_odd_vertices()
if DEBUG_FLAG:
    print("num_edges =", len(edges))
    print("odd degree vertices =", len(odd))
    print("odd vertices coords =", [V[i] for i in odd])

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
