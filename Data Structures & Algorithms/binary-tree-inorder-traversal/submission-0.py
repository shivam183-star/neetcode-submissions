# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        leftpart = self.inorderTraversal(root.left)
        leftpart.append(root.val)
        rightpart = self.inorderTraversal(root.right)
        return leftpart + rightpart
