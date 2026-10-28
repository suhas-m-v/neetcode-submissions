# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(node,maxi):
            
            if not node:
                return 0
            
            isgood =1 if node.val >= maxi else 0
            
            maxi=max(node.val,maxi)
            return isgood + traverse(node.left,maxi) + traverse(node.right,maxi)
        
        return traverse(root,float("-inf"))
         