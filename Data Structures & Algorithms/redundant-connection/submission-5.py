class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjs = [[] for _ in range(n + 1)]

        def dfs(node, parent=-1):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adjs[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)
            visit = [False] * (n + 1)

            if dfs(u):
                return [u, v]

        return []