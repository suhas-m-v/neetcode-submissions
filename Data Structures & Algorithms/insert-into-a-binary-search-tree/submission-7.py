# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
        return root
        # def search(node):
        #     if val > node.val:
        #         if not node.right:
        #             node.right = TreeNode(val)
        #             return
        #         search(node.right)
        #     if val < node.val:
        #         if not node.left:
        #             node.left = TreeNode(val)
        #             return 
        #         search(node.left)
        # if not root:
        #     return TreeNode(val)
        # search(root)
        # return root