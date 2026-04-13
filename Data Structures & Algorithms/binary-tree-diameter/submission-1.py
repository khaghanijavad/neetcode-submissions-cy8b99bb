# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def dfs(parent):
            if not parent:
                return None
            left = dfs(parent.left) if parent.left else 0
            right = dfs(parent.right) if parent.right else 0
            self.output = max(self.output, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.output
        