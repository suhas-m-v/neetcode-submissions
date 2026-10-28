# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node):
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                right_child=node.right
                lef_ext=node.left
                while lef_ext.right:
                    lef_ext=lef_ext.right
                lef_ext.right = right_child
                return node.left
        if not root:
            return None
        if root.val == key:
            return helper(root)
        
        curr = root
        while curr:
            if key > curr.val:
                if  curr.right and curr.right.val == key :
                    curr.right = helper(curr.right)
                    break
                curr = curr.right
            else:
                if curr.left and curr.left.val == key:
                    curr.left = helper(curr.left)
                    break
                curr = curr.left
        return root
            

        