# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        if not head.next: pass
        else:

            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            reverse = slow.next
            slow.next = None

            curr = reverse.next
            prev = reverse
            temp = None

            while prev:
                prev.next = temp
                temp = prev
                prev = curr
                if curr: curr = curr.next

            while head and temp:
                next1, next2 = head.next, temp.next
                head.next = temp
                temp.next = next1
                head, temp = next1, next2
            