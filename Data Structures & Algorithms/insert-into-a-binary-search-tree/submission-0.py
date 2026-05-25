# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root:
            return newNode
        node = root
        
        while True:
            if node.val < val:
                if node.right is None:
                    node.right = newNode
                    return root
                node = node.right
            else:
                if node.left is None:
                    node.left = newNode
                    return root
                node = node.left