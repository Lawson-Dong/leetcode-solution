# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    
        if list1 is None:
            return list2                 # Though return a node, we can use this node to access the whole chain
        if list2 is None:
            return list1


        if list1.val <= list2.val:
            head = list1                 # list1 is the first node of the linked list 1
            p1 = list1.next              
            p2 = list2
        if list1.val > list2.val:
            head = list2
            p2 = list2.next
            p1 = list1

        p = head

        while p1 is not None and p2 is not None:
            if  p1.val <= p2.val:
                p.next = p1              # Pay Attention to the order! We first build connection and then move p1.
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1 is not None:               # After executing the while loop, p1 is None or p2 is None, the remaining one is the last number we want
            p.next = p1
        if p2 is not None:
            p.next = p2

        return head
