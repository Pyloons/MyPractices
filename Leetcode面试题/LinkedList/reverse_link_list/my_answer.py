# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            i = head
        except:
            return None
        try:
            j = head.next
        except:
            return i
        try:
            k = j.next
        except:
            k = None
        i.next = None
        while j != None:
            j.next = i
            i = j
            j = k
            if k != None:
                k = k.next
        return i
