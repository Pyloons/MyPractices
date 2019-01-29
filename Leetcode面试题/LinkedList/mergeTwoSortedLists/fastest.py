# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
 
        if l1==None and l2==None:
            return None
        if l1==None and l2!=None:
            return l2
        if l1!=None and l2==None:
            return l1
        
        if l1.val > l2.val:
            temp = l2
            l2 = l1
            l1 = temp
        res = l1
        temp = l2
        while(l1.next!=None):
            while(l1.next!=None and l1.next.val<=temp.val):
                l1 = l1.next
            if l1.next==None:
                l1.next = temp
                return res
            else:
                temp = l1.next
                l1.next = l2
                l2 = temp
        l1.next = temp
        return res
        