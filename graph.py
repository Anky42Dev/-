from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def add_node(self, u):
        if u not in self.adj:
            self.adj[u] = []

    # ── Обходы ──────────────────────────────────────────────
    def bfs(self, start):
        visited, order = {start}, []
        q = deque([start])
        while q:
            node = q.popleft()
            order.append(node)
            for nbr, _ in self.adj[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return order

    def dfs(self, start):
        visited, order = set(), []
        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    _dfs(v)
        _dfs(start)
        return order

    # ── Кратчайшие пути ─────────────────────────────────────
    def dijkstra(self, start):
        dist = {n: float('inf') for n in self.adj}
        dist[start] = 0
        prev = {n: None for n in self.adj}
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))
        return dist, prev

    def shortest_path(self, start, end):
        dist, prev = self.dijkstra(start)
        if dist[end] == float('inf'):
            return None, float('inf')
        path, node = [], end
        while node is not None:
            path.append(node)
            node = prev[node]
        return path[::-1], dist[end]

    def bellman_ford(self, start):
        """Работает с отрицательными рёбрами. O(VE)"""
        dist = {n: float('inf') for n in self.adj}
        dist[start] = 0
        nodes = list(self.adj)
        for _ in range(len(nodes) - 1):
            for u in nodes:
                for v, w in self.adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        # проверка отрицательных циклов
        for u in nodes:
            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    raise ValueError("Negative cycle detected")
        return dist

    # ── Топологическая сортировка ────────────────────────────
    def topological_sort(self):
        """Только для DAG (ориентированный ацикличный граф)"""
        visited, stack = set(), []
        def _dfs(u):
            visited.add(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    _dfs(v)
            stack.append(u)
        for node in self.adj:
            if node not in visited:
                _dfs(node)
        return stack[::-1]

    # ── Компоненты связности ─────────────────────────────────
    def connected_components(self):
        visited, components = set(), []
        def _dfs(u, comp):
            visited.add(u)
            comp.append(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    _dfs(v, comp)
        for node in self.adj:
            if node not in visited:
                comp = []
                _dfs(node, comp)
                components.append(comp)
        return components

    def has_cycle(self):
        visited, rec_stack = set(), set()
        def _dfs(u):
            visited.add(u); rec_stack.add(u)
            for v, _ in self.adj[u]:
                if v not in visited and _dfs(v):
                    return True
                if v in rec_stack:
                    return True
            rec_stack.discard(u)
            return False
        return any(_dfs(n) for n in self.adj if n not in visited)


# ── Использование ────────────────────────────────────────────
g = Graph()
edges = [('A','B',4),('A','C',2),('B','D',3),('C','B',1),('C','D',5),('D','E',1)]
for u,v,w in edges:
    g.add_edge(u,v,w)

print(g.bfs('A'))                        # ['A','B','C','D','E']
print(g.dfs('A'))                        # ['A','B','D','E','C']
dist, _ = g.dijkstra('A')
print(dist)                              # {'A':0,'B':3,'C':2,'D':6,'E':7}
path, cost = g.shortest_path('A', 'E')
print(path, cost)                        # ['A','C','B','D','E'] 7