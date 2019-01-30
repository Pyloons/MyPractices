# Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```

层次遍历我倒是记得比较好，但是不知道为啥还是折腾了一个小时才做出这道题，很多细节上的小错误。  
还是最快那个档次的。
大致思路是先把根结点作为第一层，然后循环迭代每一层，一定要用最后一层所有的元素的左右子结点全都放进tmp[]之后，再raw.append(tmp)。这样就能在一个大list里，把每一层的元素放在一个小list里了。