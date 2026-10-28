# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def rev(hed):
            prev=None
            temp=hed
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev
        t1,t2=head,head
        prev=None
        for i in range(1,left):
            prev=t1
            t1=t1.next
        for i in range(right-1):
            t2=t2.next
        next_node=t2.next
        t2.next=None
        if prev:
            prev.next=None
        nhead=rev(t1)
        t1.next=next_node
        if prev:
            prev.next=nhead
            return head
        else:
            return nhead
        
        