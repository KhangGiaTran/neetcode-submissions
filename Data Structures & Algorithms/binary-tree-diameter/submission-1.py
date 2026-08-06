# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def recurse(curr):
            if not curr:
                return 0
            
            right = recurse(curr.right)
            left = recurse(curr.left)
            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        recurse(root)
        return self.result