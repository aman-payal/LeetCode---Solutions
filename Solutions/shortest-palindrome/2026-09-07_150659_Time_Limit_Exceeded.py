# Problem: Shortest Palindrome
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-09-07_150659 UTC
# URL: https://leetcode.com/submissions/detail/2134031549/

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
        temp_l = l
        temp_r = r
        center = (l+r)//2
        while(temp_l>=0):
            if s[temp_l] == s[temp_r]:
                temp_l-=1
                temp_r+=1
            else:
                    if l==r:
                        l-=1
                    else:
                        r-=1
                    temp_l = l
                    temp_r = r
        
        if temp_r > len(s)-1:
            return s
        while( temp_r<=len(s)-1 ):
            s = s[temp_r] + s
            temp_r+=2
        return s
