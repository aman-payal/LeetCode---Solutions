# Problem: Insert into a Binary Search Tree
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 21.1 MB
# Submitted: 2026-09-11_172737 UTC
# URL: https://leetcode.com/submissions/detail/2138808096/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif root.val > val:
            root.left =  self.insertIntoBST(root.left, val)
            return root
        else:
            root.right = self.insertIntoBST(root.right, val)
            return root
        