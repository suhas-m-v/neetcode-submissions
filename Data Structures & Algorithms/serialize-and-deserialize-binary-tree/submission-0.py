# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return ""
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(',')
        ind=1
        root = TreeNode(vals[0])
        q = deque([])
        q.append(root)
        while q:
            node = q.popleft()
            if ind < len(vals) and vals[ind] != 'null':
                node.left=TreeNode(vals[ind])
                q.append(node.left)
            ind+=1
            if ind<len(vals) and vals[ind]!= 'null':
                node.right = TreeNode(vals[ind])
                q.append(node.right)

            ind+=1
        return root



