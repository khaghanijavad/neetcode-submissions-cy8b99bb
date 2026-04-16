# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.out = ""

        def dfs(root):
            if root:
                self.out += (str(root.val) + ",")
                dfs(root.left)
                dfs(root.right)
            else:
                self.out += "N,"
        
        dfs(root)
        return self.out



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.idx = 0 

        def dfs():
            if nodes[self.idx] == "N":
                self.idx += 1
                return None
            root = TreeNode(int(nodes[self.idx]))
            self.idx += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        
    


