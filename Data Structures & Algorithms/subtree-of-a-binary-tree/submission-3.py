# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Traverse until reach root.val == subRoot.val
        # Do normal tree comparison

        def findRoot(curr):
            if not curr:
                return False
            if curr.val == subRoot.val and recurse(curr, subRoot):
                return True

            return findRoot(curr.left) or findRoot(curr.right)

        def recurse(p, q):
            if not p and not q:
                return True
            if not (p and q):
                return False
            if p.val != q.val:
                return False

            left = recurse(p.left, q.left)
            right = recurse(p.right, q.right)

            return left and right

        return findRoot(root)







