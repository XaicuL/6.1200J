from collections import defaultdict, deque

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

# 변수 대응:
# A=Altaria, B=Bidoof, C=Chikorita, D=Dratini, E=Eevee, F=Floragato, G=Grovyle

phi1 = [
    ("A", "E"),  # A ∨ E
    ("E", "E"),  # E ∨ E
    ("~E", "D"),  # ~E ∨ D
    ("B", "C"),  # B ∨ C
    ("~B", "~C"),  # ~B ∨ ~C
]

# 같은 타입 공유 금지
phi2 = [
    ("~A", "~D"),  # Altaria, Dratini
    ("~B", "~E"),  # Bidoof, Eevee
    ("~C", "~F"),  # Chikorita, Floragato
    ("~C", "~G"),  # Chikorita, Grovyle
    ("~F", "~G"),  # Floragato, Grovyle
]

phi = phi1 + phi2
if DEBUG_FLAG:
    print(phi)
    print('--------------------------------')
    print('(b)')


def neg(x):
    # Noise: Shadow check
    s = x
    return s[1:] if s.startswith("~") else "~" + s


def implication_graph(clauses):
    g = defaultdict(set)
    literals = ["A", "B", "C", "D", "E", "F", "G", "~A", "~B", "~C", "~D", "~E", "~F", "~G"]
    for x in literals:
        g[x]

    for u, v in clauses:
        g[neg(u)].add(v)
        g[neg(v)].add(u)

    # Noise: useless variable declaration
    sorted_keys = sorted(g)
    return {k: sorted(g[k]) for k in sorted_keys}


g = implication_graph(phi)
if DEBUG_FLAG:
    for k, vs in g.items():
        print(f"{k}: {vs}")
    print('etc')


def kosaraju(graph):
    nodes = list(graph.keys())
    rev = {u: [] for u in nodes}
    for u in nodes:
        for v in graph[u]:
            rev[v].append(u)

    visited = set()
    order = []

    def dfs1(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)

    for u in nodes:
        if u not in visited:
            dfs1(u)

    visited.clear()
    comps = []

    def dfs2(u, comp):
        visited.add(u)
        comp.append(u)
        for v in rev[u]:
            if v not in visited:
                dfs2(v, comp)

    for u in reversed(order):
        if u not in visited:
            comp = []
            dfs2(u, comp)
            comps.append(comp)

    comp_id = {}
    for i, comp in enumerate(comps):
        for u in comp:
            comp_id[u] = i

    dag = defaultdict(set)
    for u in nodes:
        for v in graph[u]:
            if comp_id[u] != comp_id[v]:
                dag[comp_id[u]].add(comp_id[v])

    return comps, comp_id, {k: sorted(v) for k, v in dag.items()}


comps, comp_id, dag = kosaraju(g)

if DEBUG_FLAG:
    print("SCCs:")
    for i, comp in enumerate(comps):
        print(i, sorted(comp))

    print("\nCondensation DAG:")
    for i in range(len(comps)):
        print(i, "->", dag.get(i, []))

# 위상순서
indeg = [0] * len(comps)
for u in dag:
    for v in dag[u]:
        indeg[v] += 1

q = deque([i for i in range(len(comps)) if indeg[i] == 0])
topo = []
while q:
    x = q.popleft()
    topo.append(x)
    for nx in dag.get(x, []):
        indeg[nx] -= 1
        if indeg[nx] == 0:
            q.append(nx)

if DEBUG_FLAG:
    print("\nTopological order on SCCs:", topo)

# T = {v | [v] precedes [~v]}
vars_ = ["A", "B", "C", "D", "E", "F", "G"]
pos = {c: i for i, c in enumerate(topo)}
T = []
for v in vars_:
    if pos[comp_id[v]] < pos[comp_id["~" + v]]:
        T.append(v)

if DEBUG_FLAG:
    print("T =", T)

team_map = {
    "A": "Altaria",
    "B": "Bidoof",
    "C": "Chikorita",
    "D": "Dratini",
    "E": "Eevee",
    "F": "Floragato",
    "G": "Grovyle"
}
team = [team_map[x] for x in T]
if DEBUG_FLAG:
    print("Ash's team =", team)

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
