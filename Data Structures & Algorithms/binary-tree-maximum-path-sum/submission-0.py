# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def sumPath(node):
            nonlocal maxSum
            if not node:
                return 0
            leftSum = sumPath(node.left)
            rightSum = sumPath(node.right)
            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)
            maxSum = max(maxSum, leftSum + rightSum + node.val)

            return max(leftSum,rightSum) + node.val


        sumPath(root)
        return maxSum
