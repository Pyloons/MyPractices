'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

此题过于基础
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        i = 0
        length = len(s) / 2
        while i < length:
            s[i], s[-i-1] = s[-i-1], s[i]
            i += 1


'''
评论区大概有三种思路：递归、经典、Pythonic。
其中由于题中明确提出不使用return直接修改原字符串，所以
递归在此题中难以应用，倒是Pythonic很好用


class SolutionPythonic(object):
    def reverseString(self, s):
        s[:] = s[::-1]


class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])
'''