# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        p1 = l1
        p2 = l2
        carry = 0

        dummy = ListNode(0)
        current = dummy

        while p1 or p2 or carry:

            val_1 = p1.val if p1 else 0
            val_2 = p2.val if p2 else 0

            total = val_1 + val_2 + carry

            carry = total // 10
            digit = total % 10

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

            current.next = ListNode(digit)
            current = current.next

        return dummy.next
