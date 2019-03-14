# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.right == None and root.left == None:
            return 1 
        elif root.right == None:
            return 1+self.maxDepth(root.left)
        elif root.left == None:
            return 1+self.maxDepth(root.right)
        else:
             return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
