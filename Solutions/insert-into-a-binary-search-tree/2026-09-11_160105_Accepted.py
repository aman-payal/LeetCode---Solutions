# Problem: Insert into a Binary Search Tree
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 21.2 MB
# Submitted: 2026-09-11_160105 UTC
# URL: https://leetcode.com/submissions/detail/2138716616/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        prev =  None
        if root == None:
            return new_node
        start = root
        while root != None:
            if val < root.val:
                prev = root
                root = root.left

            elif val > root.val:
                prev = root
                root =  root.right 
        if prev.val > val:
            prev.left = new_node
        else:
            prev.right = new_node
        return start


        
        