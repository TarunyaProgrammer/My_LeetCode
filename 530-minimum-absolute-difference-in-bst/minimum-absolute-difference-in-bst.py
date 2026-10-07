# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini = float('inf')
        prev = None

        def traverse(root):
            nonlocal mini, prev

            if root == None: return
            traverse(root.left)

            if prev is not None:
                mini = min(mini, root.val - prev)
            prev = root.val

            traverse(root.right)

        traverse(root)
        return mini