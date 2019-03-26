'''
即二叉树先序遍历
有进一步要求使用迭代法遍历
这里都是我的答案
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MyIterativelySolution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result = []
        
        node = root
        store = []
        while node or store:
            if node:
                if node.right:
                    store.append(node.right)
                result.append(node.val)
                node = node.left
            else:
                node = store.pop()
        return result
        
class MyRecursivelySolution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result = []
        
        def recursion_pre(node):
            nonlocal result
            if not node:
                return
            else:
                result.append(node.val)
                recursion_pre(node.left)
                recursion_pre(node.right)
                
        recursion_pre(root)
        return result