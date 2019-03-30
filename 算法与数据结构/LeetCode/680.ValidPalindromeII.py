'''
680. Valid Palindrome II
Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class OfficialSolutionImproved:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        def is_pali_range(i, j):
            return s[i:j+1] == s[i:j+1][::-1]
        
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return is_pali_range(lo+1,hi) or is_pali_range(lo, hi-1)
            lo += 1
            hi -= 1
        