# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        current = head
        stack = []

        while current:
            n += 1
            current = current.next
            
        stack_size = n // 2
        skip = n - stack_size

        current = head
        for i in range(skip):
            if i == skip - 1:
                next = current.next
                current.next = None
                current = next
            else:
                current = current.next
        while current:
            stack.append(current)
            current = current.next

        
        current = head
        while stack:
            next = current.next
            insert_node = stack.pop()
            current.next = insert_node
            insert_node.next = next
            current = next
    
        
        
        
