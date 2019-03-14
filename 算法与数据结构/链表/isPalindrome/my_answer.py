# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        
        while head != None:
            stack.append(head.val)
            head = head.next
            
        return True if stack == stack[::-1] else False
