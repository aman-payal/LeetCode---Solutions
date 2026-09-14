# Problem: Count Commas in Range II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-09-13_153500 UTC
# URL: https://leetcode.com/submissions/detail/2140748043/

class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if n==10000:
            return 1
        total_commas = 1
        
        if n>=1000000:
            total_commas =  999000 + 2
        else:
            return (n-999)
        if n>=1000000000:
            total_commas += (2 *999000000)+1
        else:
            return total_commas + 2*(n-1000000)
        if n>=1000000000000:
            total_commas += (3*999000000000)+1
        else:
            return total_commas+3*(n-1000000000)
        if n>=1000000000000000:
            total_commas+=(4*999000000000000)+1
        else:
             return total_commas+4*(n-1000000000000)
        return total_commas
        


        
