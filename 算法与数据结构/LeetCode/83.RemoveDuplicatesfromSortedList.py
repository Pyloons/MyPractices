'''
83. Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MySolution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        
        ptr = head
        diff_ptr = head.next
        store_val = head.val
        
        while diff_ptr:
            if store_val == diff_ptr.val:
                diff_ptr = diff_ptr.next
            else:
                ptr.next = diff_ptr
                ptr = diff_ptr
                store_val = diff_ptr.val
                diff_ptr = diff_ptr.next
        ptr.next = None
        return head
        