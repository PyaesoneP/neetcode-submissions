# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        head1 = list1
        head2 = list2

        if head1.val < head2.val:
            head = head1
        else:
            head = head2

        current1 = head1
        current2 = head2

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next

            if next1 and next2:
                if next1.val < next2.val:
                    lower = next1
                else:
                    lower = next2
            elif next1:
                lower = next1
            else:
                lower = next2

            if next1 and next1.val < current2.val:
                current1 = next1
                continue
            elif next2 and next2.val < current1.val:
                current2 = next2
                continue
            
            if current1.val < current2.val:
                current1.next = current2
                current2.next = lower
            else:
                current2.next = current1
                current1.next = lower
            
            current1 = next1
            current2 = next2

        return head