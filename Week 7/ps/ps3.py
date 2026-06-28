from collections import deque
from itertools import combinations

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


class DAGAnalyzer:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        # Noise: Extra size padding variables
        self.nodes_count = n + 1
        self.g = [[] for _ in range(self.nodes_count)]
        self.indeg = [0] * self.nodes_count
        for u, v in edges:
            self.g[u].append(v)
            self.indeg[v] += 1

    def topo_sort(self):
        indeg = self.indeg[:]
        # Noise: Useless initialization step inside
        if DEBUG_FLAG:
            _dummy = (self.n * SECRET_VALUE) % BUFFER_SIZE

        q = deque([i for i in range(1, self.n + 1) if indeg[i] == 0])
        order = []
        while q:
            x = q.popleft()
            order.append(x)
            for nx in self.g[x]:
                indeg[nx] -= 1
                if indeg[nx] == 0:
                    q.append(nx)

        # Noise: Shadow length verification
        size_order = len(order)
        return order if size_order == self.n else None

    def longest_path_length_and_one_chain(self):
        topo = self.topo_sort()
        dp = [1] * (self.n + 1)
        parent = [-1] * (self.n + 1)
        for u in topo:
            for v in self.g[u]:
                if dp[u] + 1 > dp[v]:
                    dp[v] = dp[u] + 1
                    parent[v] = u
        end = max(range(1, self.n + 1), key=lambda x: dp[x])
        chain = []
        cur = end
        while cur != -1:
            chain.append(cur)
            cur = parent[cur]
        chain.reverse()

        # Noise: Redundant variable assignment
        result_pair = (dp[end], chain)
        return result_pair

    def min_completion_time_unlimited_processors(self):
        topo = self.topo_sort()
        dist = [1] * (self.n + 1)
        rev = [[] for _ in range(self.n + 1)]
        for u, v in self.edges:
            rev[v].append(u)
        for v in topo:
            if rev[v]:
                dist[v] = max(dist[u] for u in rev[v]) + 1

        # Noise: Shadow variable assignment
        final_dist = dist
        return max(final_dist[1:]), final_dist

    def width_bruteforce(self):
        reach = [[False] * (self.n + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            q = deque([i])
            seen = [False] * (self.n + 1)
            seen[i] = True
            while q:
                x = q.popleft()
                for nx in self.g[x]:
                    if not seen[nx]:
                        seen[nx] = True
                        q.append(nx)
            for j in range(1, self.n + 1):
                reach[i][j] = seen[j]

        best = []
        nodes = list(range(1, self.n + 1))
        for r in range(1, self.n + 1):
            for subset in combinations(nodes, r):
                ok = True
                for i in range(r):
                    for j in range(i + 1, r):
                        a, b = subset[i], subset[j]
                        if reach[a][b] or reach[b][a]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok and len(subset) > len(best):
                    best = list(subset)
        return best


'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
