# Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
```
Input: haystack = "hello", needle = "ll"
Output: 2
```
Example 2:
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```
Clarification:

* What should we return when needle is an empty string? This is a great question to ask during an interview.
* For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

***
这道题我并没有做出来。我第一眼就知道这玩意要用模式匹配，KMP应该是最佳方案，但是我仔细回忆了一下，我发现自己连next数组怎么算都忘了，所以打算依靠Python的语法糖来解决，无奈最后陷入if-else地狱，决定看看答案。  
intro_practise.py就是高赞python版答案。说白了就是个简单匹配，74个测试平均36毫秒。  
mad_code.py里的代码，同样的简单匹配，74个测试平均32毫秒。  
字符串匹配还是要加强一下。