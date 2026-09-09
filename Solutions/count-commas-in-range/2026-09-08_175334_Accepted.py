# Problem: Count Commas in Range
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Submitted: 2026-09-08_175334 UTC
# URL: https://leetcode.com/submissions/detail/2135478887/

class Solution:
    def countCommas(self, n: int) -> int:
        return max(n-999, 0)