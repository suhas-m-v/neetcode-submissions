# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(temp):
            prev=None
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev
        def findkthnode(temp,k):
            while temp and k>1:
                k-=1
                temp=temp.next
            return temp
        temp=head
        prev_node=None
        while temp:
            kthnode=findkthnode(temp,k)
            if kthnode is None:
                if prev_node:
                    prev_node.next=temp
                    break
            next_node=kthnode.next
            kthnode.next=None
            nhead=rev(temp)
            if temp==head:
                head=nhead
            else:
                prev_node.next=nhead
            
            prev_node=temp
            temp=next_node
        return head
