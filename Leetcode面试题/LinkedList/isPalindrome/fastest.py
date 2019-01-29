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
        prev = None
        fast = slow = head
        # 翻转链表的前n/2个结点
        while fast and fast.next:
            fast = fast.next.next
            prev, prev.next, slow = slow, prev, slow.next
        # 结点个数为奇数时，跳过最中间的结点
        if fast:
            slow = slow.next
        # 前n/2个结点翻转后，与剩下的结点进行对比
        # 移动指针，
        while slow and slow.val == prev.val:
            # 两个节点同时后移
            prev, slow = prev.next, slow.next
        return not prev
