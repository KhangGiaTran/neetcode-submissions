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

        if not root:
            return False
        if not subRoot:
            return True

        def findRoot(curr):
            if not curr:
                return False
            if curr.val == subRoot.val and sameTree(curr, subRoot):
                return True

            return findRoot(curr.left) or findRoot(curr.right)

        def sameTree(p, q):
            if not p and not q:
                return True
            if not (p and q):
                return False
            if p.val != q.val:
                return False

            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)

            return left and right

        return findRoot(root)







