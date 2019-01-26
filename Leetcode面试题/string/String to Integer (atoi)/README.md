# String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"  
Output: 42

Example 2:

Input: "   -42"  
Output: -42  
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"  
Output: 4193  
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"  
Output: 0  
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"  
Output: -2147483648  
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.


# 关于这道atoi我没有什么好说的
最开始还妄想用if-else解决，最后连error_input_list =[...]这种招数都用上来了，根本匹配不完，不用正则表达式根本做不出来。  
而且正则表达式运行他们一千多条测试也就60ms上下，还算快。

他们用来测试的太多种类的字符串，五个Example根本无法涵盖，他们想要什么答案我们这些刷题的根本不知道，只能跟着测试结果去猜。

我在讨论区的评价是：
>I made it in re:)  
>And it paid my 2 hour to try what answer they want（^_^）凸  
>Do not ask how I find the pattern,I just try it in many many many time.

这道题的讨论区是炸锅的，最高投票的答案是高呼“这是道沙*题”，第二高的答案是用C语言写的，没用正则，if-else眼花缭乱；第三高的答案是Java写的，据评论圈，根本跑不通测试……  

但还是找到了几个用re的小兄弟，而且似乎答案比我简单太多，速度快我8毫秒，所以还是记下来了；山不在高，好答案不看投票。

另外，如果不用re，则要好好使用strip()和isdigits()