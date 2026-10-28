# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i in range(len(lists)):
            heapq.heappush(heap,(lists[i].val,i,lists[i]))
        dum=ListNode()
        temp=dum
        while heap:
            val,ind,node=heapq.heappop(heap)
            temp.next=node
            temp=node
            if node.next:
                heapq.heappush(heap,(node.next.val,ind,node.next))
        return dum.next
            