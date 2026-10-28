# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode()
        dummy=dum
        l1h=l1
        l2h=l2
        tot=0
        carry=0
        while l1h or l2h:
            tot=carry
            if l1h:
                tot+=l1h.val
                l1h=l1h.next
            if l2h:
                tot+=l2h.val
                l2h=l2h.next
            nn=ListNode(tot%10)
            dummy.next=nn
            dummy=dummy.next
            carry=tot//10
        if carry:
            nn=ListNode(carry)
            dummy.next=nn
            dummy=dummy.next
        return dum.next