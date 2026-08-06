# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def recurse(curr, maxVal):
            if not curr:
                return

            if curr.val >= maxVal:
                self.count += 1
            maxVal = max(maxVal, curr.val)

            left = recurse(curr.left, maxVal)
            right = recurse(curr.right, maxVal)

        recurse(root, float('-infinity'))
        return self.count