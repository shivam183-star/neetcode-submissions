# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         
        def dfs(node, currentMax):
            if not node:
                return 0
            good = 0
            if node.val >= currentMax:
                good = 1
                currentMax = node.val
            return good + dfs(node.left, currentMax) + dfs(node.right, currentMax)
        
        return dfs(root, root.val)