# Problem: Search in a Binary Search Tree
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 21 MB
# Submitted: 2026-09-10_185207 UTC
# URL: https://leetcode.com/submissions/detail/2137879649/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def dfs(self, parent, result):
    #     if parent == None:
    #         return
        
    #     result.append(parent.val)
    #     self.dfs(parent.left, result)
    #     self.dfs(parent.right, result)



    def search_val(self, parent, val):
        if parent == None:
            return None
        if parent.val == val:
            return parent
        if val < parent.val:
           return  self.search_val(parent.left, val)
        else:
            return self.search_val(parent.right, val)



    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
   
        return self.search_val(root, val)
        