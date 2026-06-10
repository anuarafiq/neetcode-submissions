# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head
        ptr1 = l1
        ptr2 = l2
        carry = 0

        while ptr1 or ptr2 or carry:
            summ = (ptr1.val if ptr1 else 0) + (ptr2.val if ptr2 else 0)  + carry
            carry = summ // 10
            ptr.next = ListNode(val = summ % 10)
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            ptr = ptr.next

        return head.next