# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def rightView(node,depth):
            if not node:
                return 
            if len(ans) == depth:
                ans.append(node.val)
            
            rightView(node.right,depth+1)
            rightView(node.left,depth+1)
        rightView(root,0)
        return ans