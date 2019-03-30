'''
563. Binary Tree Tilt
Easy

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MySolutionImproveByOfficialAnswer:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # tilts = []
        tilts = 0
        
        def travel(node):
            nonlocal tilts
            if not node:
                return 0
            else:
                left = travel(node.left)
                right = travel(node.right)
                # 给tilt加上这个节点的值
                tilts += abs(left - right)
                # 给上层结点返回这个结点的总和值，供父节点计算自己的tilt
                return left + right + node.val
        
        # def make_tilts(node):
        #     if node.left:
        #         make_tilts(node.left)
        #     if node.right:
        #         make_tilts(node.right)
        #     tilt_left = travel(node.left)
        #     tilt_right = travel(node.right)
        #     tilts.append(abs(tilt_left - tilt_right))
            
        # make_tilts(root)
        travel(root)
        return tilts
        