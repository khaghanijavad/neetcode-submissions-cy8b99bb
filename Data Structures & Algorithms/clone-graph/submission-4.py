"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}

        def dfs(node):
            if node in visit:
                return visit[node]
            
            clone = Node(node.val)
            visit[node] = clone

            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))

            return visit[node]

        return dfs(node) if node else None