"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)

        visit = {}
        visit[node] = Node(node.val)
        
        
        def bfs(node_curr):
            q = collections.deque()
            q.append(node_curr)
            while q:
                nodee = q.popleft()
                for n in nodee.neighbors:
                    if n not in visit:
                        visit[n] = Node(n.val)
                        visit[n].neighbors= []
                        q.append(n)
                
                    visit[nodee].neighbors.append(visit[n])
        
        bfs(node)
        return visit[node]