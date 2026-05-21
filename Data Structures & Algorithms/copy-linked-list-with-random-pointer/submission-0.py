"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None: None}

        temp = head
        while temp:
            newNode = Node(temp.val)
            mapping[temp] = newNode
            temp = temp.next

        temp = head
        while temp:
            newNode = mapping[temp]
            newNode.next = mapping[temp.next]
            newNode.random = mapping[temp.random]
            temp = temp.next
        
        return mapping[head]
