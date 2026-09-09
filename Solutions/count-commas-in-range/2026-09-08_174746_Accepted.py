# Problem: Count Commas in Range
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Submitted: 2026-09-08_174746 UTC
# URL: https://leetcode.com/submissions/detail/2135470831/

class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if n==1000:
            return 1
        i = 1000000
        prev_stop = 1000
        total_comma_count = 0
        comma_count_in_one_int = 1
        while(i<=n):
            comma_count_in_one_int += 1
            total_comma_count += (i-prev_stop) * comma_count_in_one_int
            prev_stop = i
            i *= 1000
        total_comma_count += (n - prev_stop + 1) * comma_count_in_one_int
        return total_comma_count
        
