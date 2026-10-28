# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                search(node.right)
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return 
                search(node.left)
        if not root:
            return TreeNode(val)
        search(root)
        return root