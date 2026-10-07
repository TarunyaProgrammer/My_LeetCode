class Solution:

    def isValidBST(self, root: TreeNode | None) -> bool:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(vals) - 1):
            if vals[i] >= vals[i + 1]:
                return False

        return True