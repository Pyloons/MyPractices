# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        stack = []
        prev = None
        p = root
        while len(stack) > 0 or p is not None:
            while p is not None:
                stack.append(p)
                p = p.left
            if len(stack) > 0:
                p = stack.pop()
                if prev == None:
                    prev = p
                elif p.val <= prev.val:
                    return False
                else:
                    prev = p
                p = p.right
        return True
        