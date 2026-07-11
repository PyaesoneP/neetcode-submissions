# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2

        dummy = ListNode()
        current = dummy

        carry = 0

        while pointer1 or pointer2:
            val1 = pointer1.val if pointer1 else 0
            val2 = pointer2.val if pointer2 else 0
            node_sum = val1 + val2 + carry
            carry = node_sum // 10
            current.next = ListNode(node_sum % 10)
            current = current.next
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None

        current.next = ListNode(carry) if carry else None
        return dummy.next