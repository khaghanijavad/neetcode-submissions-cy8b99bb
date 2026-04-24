from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def dfs(src: int, target: int, visited: set) -> bool:
            if src == target:
                return True

            visited.add(src)

            for nei in graph.get(src, []):
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for u, v in edges:
            # Check if u and v are already connected
            if u in graph and v in graph:
                if dfs(u, v, set()):
                    return [u, v]

            # Add edge to graph
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)