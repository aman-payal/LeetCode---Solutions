# Problem: Rotate List
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Submitted: 2026-09-16_181852 UTC
# URL: https://leetcode.com/submissions/detail/2144003171/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 0 or head == None or head.next == None:
            return head
        
        l = 0
        p = head
        while p is not None:
            l+=1
            p=p.next
        count = 0
        k = k%l
        while count < k:
            prev = None
            curr = head
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = head
            head = curr
            count += 1

        return head


