# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []

        dummy = ListNode()

        current = dummy

        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            node = heapq.heappop(heap)
            current.next = node
            current = node

            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next
        