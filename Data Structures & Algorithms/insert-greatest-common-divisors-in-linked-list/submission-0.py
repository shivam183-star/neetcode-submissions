# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def gcd(self, x, y):
        for i in range(min(x, y), 0, -1):
            if x % i == 0 and y % i == 0:
                return i

    def insertGreatestCommonDivisors(self, head):
        left = head

        while left.next:
            right = left.next
            val = self.gcd(left.val, right.val)
            node = ListNode(val)
            node.next = right
            left.next = node

            left = right

        return head