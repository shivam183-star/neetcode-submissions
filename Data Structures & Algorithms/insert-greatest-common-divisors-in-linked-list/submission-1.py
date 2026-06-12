# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

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