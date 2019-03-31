'''
338. Counting Bits
Medium

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
# 详见http://www.cnblogs.com/grandyang/p/5294255.html
# 仔细观察二进制的规律是最重要的
# 就是没看出来这跟动态规划有个什么毛线关系
class SomeOneSolution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for x in range(1, num + 1):
            res[x] = res[(x&(x-1))]+1
        return res