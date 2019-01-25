# First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

## Examples:

```
s = "leetcode"
return 0.
```

```
s = "loveleetcode",
return 2.
```

> Note: You may assume the string contain only lowercase letters. 

# 我的思路
关于这道题，我走了个常规路线：
1. 首先建立一个计数用的字典
2. 一个字符一个字符查字典，第一个值为1的字符的下标就是答案
3. 默认找不到返回-1
这样的算法理论时间复杂度为O(2n)

# 高票答案
首先这个答案自定义一串小写字符串已经被人吐槽了，应该用`string.ascii_lowercase`才更优雅更Python。  
另外，这个答案里使用了s.count()来计数。从理论上讲，这种功能的内置函数调用会增加运行时间，降低算法效率。但实际上速度却比我的O(2n)要块得多。实测我的算法用了172毫秒，高票用了56毫秒（使用.ascii_lowercase也是一样的）。  
评论圈的解释是这种内置函数是用C语言写的，所以时间复杂度虽然高，但是运行速度非常快。

# 感想
学会C和Python混合编程是多么重要。