# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []

        def recurse(curr, depth):
            if not curr:
                return
            if len(self.result) - 1 < depth:
                self.result.append([])
            recurse(curr.left, depth + 1)
            recurse(curr.right, depth + 1)
            self.result[depth].append(curr.val)

        recurse(root, 0)
        return self.result