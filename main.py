"""
HW04 — Peaceful Teams (Bipartite Check)

Implement:
- bipartition(graph)
"""

from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if bipartite; else None.

    Use BFS coloring over all components.

    Hints:
    - Maintain color: dict node -> 0/1
    - On seeing same-color neighbors, return None
    """
    color = {}

    for start in graph:
        if start in color:
            continue

        color[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            for v in graph.get(u, []):
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return None

    left = {node for node, c in color.items() if c == 0}
    right = {node for node, c in color.items() if c == 1}

    return (left, right)
