class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Empty graph is tree
        if n == 0:
            return True

        # Tree requirement: No cycle, connected
        if len(edges) != n - 1:
            return False

        visited = set()
        graphMap = {i: [] for i in range(n)}

        for node1, node2 in edges:
            graphMap[node1].append(node2)
            graphMap[node2].append(node1)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for adj in graphMap[node]:
                if adj == parent:
                    continue
                if not dfs(adj, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n