# Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

> Note: A leaf is a node with no children.

Example:
```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
```

没啥好说的，二叉树深度，递归就好。
最佳答案是44ms，我是48ms，多了两个判定做剪枝肯定是快一些。