# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.level_count(root)

    def level_count(self, parent, depth=0):
        if parent:
            depth += 1
        
            if parent.left:
                depth_left = self.level_count(parent.left, depth)
            else:
                depth_left = depth
            
            if parent.right:
                depth_right = self.level_count(parent.right, depth)
            else:
                depth_right = depth
            return max(depth_left, depth_right)
        return depth        