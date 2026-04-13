# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        return self.swap_nodes(root)

    def swap_nodes(self, parent):
        if parent:
            temp = parent.left
            parent.left = parent.right
            parent.right = temp
            self.swap_nodes(parent.left)
            self.swap_nodes(parent.right)
        return parent