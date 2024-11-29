# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Taking care of edge cases
        if not p and not q: # If both trees are empty then they are technically equal
            return True
        if not p or not q or p.val != q.val: # If only one is empty, or the values don't match, they're not euqal
            return False
        # The function will call itself for each not=de to the left and to the right of the tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.righ)
