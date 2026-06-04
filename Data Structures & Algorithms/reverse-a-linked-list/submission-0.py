# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        curr = head.next
        prev = head
        temp = None

        while prev:
            prev.next = temp
            temp = prev
            prev = curr
            if curr: curr = curr.next

        return temp