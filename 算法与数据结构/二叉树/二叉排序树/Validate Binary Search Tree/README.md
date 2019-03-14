# Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:
```
Input:
    2
   / \
  1   3
Output: true
```
Example 2:
```
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
```


这道题我处在Beat 100%的位置。  
原因是我不会做（这么基础都不会做，你咋不去xxxx)，讨论区也没有靠谱的答案，然后百度了一下思路，发现我最开始想的，递归比较左右子结点的值是错误思路。  
正确的思路是中序遍历。中序遍历的过程正是二叉查找树所有结点从小到大访问的顺序。  
最开始我用递归访问，然后遇到了一个只有左子树的上万深度的“二叉树”，递归被退出。  
再然后就是非常折腾的两个小时，我一直在回忆如何用迭代中序遍历二叉树，无果，翻书，找到了方法，把书上的C语言翻译成Python，通过。
***
其实迭代中序遍历的思路也非常简单，只要记住：  
大方向是用一个指针p把本结点及所有左子结点入栈。  
如果左边没有了，就出个栈，用p接着，做一些处理，然后p指向右边。  
右边如果不为空，就把右边当成新的根节点继续往栈里压入；如果为空，就看栈里还有没有结点，如果还有，就出一个让p接着，继续上面的处理。
如果p也为None了，栈也空了，这是真访问完了……
然后由于遍历结果是一个结点按值从小到大排列的序列，所以其实只需要用一个变量记录前一个出栈结点的值是不是比现在出栈结点的值小，如果是，就继续遍历，如果不是，就可以返回False了。