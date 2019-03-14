# Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
```
      0
     / \
   -3   9
   /   /
 -10  5
```

这个题其实是之前验证二叉查找树思路的逆向。  
验证一颗二叉树是不是二叉查找树，靠中序遍历形成某种形式的有序序列，然后就可以验证该序列的有序性；  
这道题是已经证实序列有序性，用何种方法可以反推符合该序列的二叉查找树。  
说到有序序列，我就想起折半排序（花我就不开了）……  
如图：
```
站起来的时候：
      0
     / \
   -3   9
   /   /
 -10  5
拍扁的时候：
             _
-10 — -3 — 0 5 — 9
```
要把拍扁的序列一个一个提起来，折半的思想刚刚好

最快的那个答案看起来是预处理了一些无理答案，实际上减少了递归次数，提高了效率。
