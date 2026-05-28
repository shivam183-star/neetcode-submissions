# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0

        def build(left, right):
            nonlocal pre_index
            if left > right:
                return None
            
            node = TreeNode(preorder[pre_index])
            pre_index += 1

            mid = inorder.index(node.val)

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node
        
        return build(0, len(inorder) - 1)