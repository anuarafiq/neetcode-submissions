# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2): return None
        if not list1: return list2
        if not list2: return list1

        l1 = list1
        l2 = list2
        ptr = ListNode()
        head = ptr

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2
            
        return head.next
