class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphMap = {}
        visit = set()

        def dfs(src, trg):
            if src == trg:
                return True
            
            visit.add(src)

            adjs = graphMap[src]
            for adj in adjs:
                if adj not in visit:
                    if dfs(adj, trg):
                        return True
            return False


        for u, v in edges:
            if u in graphMap and v in graphMap:
                visit = set()
                if dfs(u, v):
                    return [u, v]

            if u not in graphMap:
                graphMap[u] = []
            if v not in graphMap:
                graphMap[v] = []
            graphMap[u].append(v)
            graphMap[v].append(u)