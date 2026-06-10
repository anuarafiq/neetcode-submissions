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

        while ptr1 and ptr2:
            summ = ptr1.val + ptr2.val + carry
            carry = summ // 10
            ptr.next = ListNode(val = summ % 10)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            ptr = ptr.next


        ptr.next = ptr1 or ptr2 or (ListNode(val = carry) if carry else None)

        return head.next