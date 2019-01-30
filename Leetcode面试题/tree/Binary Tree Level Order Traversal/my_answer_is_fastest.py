# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        raw = [[root],]
        while True:
            tmp = []
            for i in raw[-1]:
                if i.left is not None:
                    tmp.append(i.left)
                if i.right is not None:
                    tmp.append(i.right)
                i = i.val
            if len(tmp) <= 0:
                break
            raw.append(tmp)
        return [[x.val for x in i] for i in raw]
        