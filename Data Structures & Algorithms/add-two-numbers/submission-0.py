# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode()
        c = 0
        prev = dummy
        while temp1 or temp2:
            newNode = ListNode()
            if not temp1:
                sum = temp2.val + c
            elif not temp2:
                sum = temp1.val + c
            else:
                sum = temp1.val + temp2.val + c
            if sum >= 10:
                sum -= 10
                c = 1
            else:
                c = 0
            newNode.val = sum
            prev.next = newNode
            prev = newNode
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        
        if c == 1:
            last = ListNode(1)
            prev.next = last
        return dummy.next

