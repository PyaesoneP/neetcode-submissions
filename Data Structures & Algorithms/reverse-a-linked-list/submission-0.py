# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        while current:
            previous = current
            next_node = current.next
            previous.next = None if current == head else old_previous
            old_previous = current
            current = next_node

        return previous
        