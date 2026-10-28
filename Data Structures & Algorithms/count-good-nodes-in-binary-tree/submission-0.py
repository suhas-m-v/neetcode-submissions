# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def traverse(node,maxi):
            nonlocal count
            if not node:
                return
            
            if node.val >= maxi:
                count += 1
                maxi=max(node.val,maxi)
            traverse(node.left,maxi)
            traverse(node.right,maxi)
        
        traverse(root,float("-inf"))
        return count