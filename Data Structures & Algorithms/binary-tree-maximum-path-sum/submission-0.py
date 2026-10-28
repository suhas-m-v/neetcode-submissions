# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float("-inf")
        def maxpath(node):
            nonlocal maxi
            if not node:
                return 0
            
            left = max(0, maxpath(node.left))
            right = max(0, maxpath(node.right))

            maxi = max(maxi, node.val+left+right)

            return node.val + max(left,right)
        maxpath(root)
        return maxi
        