# Problem: Rotate List
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-09-16_181517 UTC
# URL: https://leetcode.com/submissions/detail/2143998766/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 0 or head == None or head.next == None:
            return head
        
        count = 0

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


