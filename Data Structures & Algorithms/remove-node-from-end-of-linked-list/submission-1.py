# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        ptr = head
        if length == 1: return None
        if length == n: return head.next
        
        for _ in range(length-n-1):
            ptr = ptr.next

        ptr.next = ptr.next.next
        return head

        