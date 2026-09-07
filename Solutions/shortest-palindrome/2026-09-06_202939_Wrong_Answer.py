# Problem: Shortest Palindrome
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-09-06_202939 UTC
# URL: https://leetcode.com/submissions/detail/2133276357/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return s
        l=0
        r=len(s)-1
        while( l<=r ):
            l+=1
            r-=1
        l-=1
        r+=1

        while(l>=0):
            if s[l] == s[r]:
                l-=1
                r+=1
            else:
                if r-l == 1:
                    l-=1
                else:
                    r=l+1

        
        if r > len(s)-1:
            return s
        while( r<=len(s)-1 ):
            s = s[r] + s
            r+=2
        return s
