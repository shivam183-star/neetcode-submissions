# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rootpart = [root.val]
        leftpart = self.preorderTraversal(root.left)
        
        rightpart = self.preorderTraversal(root.right)
        return rootpart + leftpart + rightpart