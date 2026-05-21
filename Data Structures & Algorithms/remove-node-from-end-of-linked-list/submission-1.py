# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        i = 0
        while fast:
            fast = fast.next
            i += 1
            if i > n+1:
                slow = slow.next
           
        slow.next = slow.next.next
        return dummy.next