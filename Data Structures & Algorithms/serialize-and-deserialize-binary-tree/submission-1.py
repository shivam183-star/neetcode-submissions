# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        pre = []

        def preorder(root):
            if not root:
                pre.append("N")
                return
            
            pre.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        data = ",".join(pre)
        return data

        

    def deserialize(self, data):
        preorder = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            if preorder[index] == "N":
                index += 1
                return
            
            node = TreeNode(int(preorder[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
            