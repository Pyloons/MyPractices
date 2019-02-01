# First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
```
仍然是折半思想，大致思路没错，但是不知道为什么总是跑不到正确的答案上。
参考了讨论圈，把调整right=mid-1变成了right=mid之后就好了。否则n=3，expect=1总是错的。
自己的理解是，在数字比较小的时候，left跟mid很可能脸贴脸，如果调整right是mid-1的话，那么right跟left就会相等，在下一步寻找正解之前，循环就会结束。
所以以后使用折半思想的时候要注意，在查找某个位置是否符合要求的时候，如果出现了没查找完就结束的情况，一定要及时调整left和right。