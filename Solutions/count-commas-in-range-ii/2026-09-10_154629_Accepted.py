# Problem: Count Commas in Range II
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Submitted: 2026-09-10_154629 UTC
# URL: https://leetcode.com/submissions/detail/2137661414/

class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if n==1000:
            return 1
        total_comma = 0
        comma_count_in_one_int = 0
        i = 1000
        while i<=n:
            total_comma += (comma_count_in_one_int * (i - (i//1000)))
            comma_count_in_one_int += 1
            i *= 1000
        i //= 1000
        
        total_comma += (n-i+1)*comma_count_in_one_int
        return total_comma

        
