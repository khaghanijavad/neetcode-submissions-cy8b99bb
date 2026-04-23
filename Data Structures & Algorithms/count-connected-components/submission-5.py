class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graphMap[node1].append(node2)
            graphMap[node2].append(node1)
        visit = set()
        nComp = 0 


        def dfs(node, parent = -1):
            visit.add(node)
            adjs = graphMap[node]
            for adj in adjs:
                if adj != parent and adj not in visit:
                    dfs(adj, node)
            

        for i in range(n):
            if i not in visit:
                nComp += 1
                dfs(i)
        return nComp