'''
823. Binary Trees With Factors
Medium

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Note:

1 <= A.length <= 1000.
2 <= A[i] <= 10 ^ 9.
'''
class Solution:
    def numFactoredBinaryTrees(self, A: 'List[int]') -> 'int':
        # 题干要求的模数
        MOD = 10 ** 9 + 7
        # A的长度
        N = len(A)
        # 给A排序
        A.sort()
        # A这么长的dp表
        dp = [1] * N
        # 对A按值取下标的索引
        index = {x: i for i, x in enumerate(A)}
        # 枚举取A中的数与该数的下标
        for i, x in enumerate(A):
            # 每针对一个下标，取（该下标）个数来循环
            for j in range(i):
                # 如果当前大循环中的数可被小循环中的数整除
                if x % A[j] == 0:
                    # 计算他们的倍数
                    right = x // A[j]
                    # 如果他们的倍数在索引中
                    if right in index:
                        # dp表的i位置增加dp表j位置与dp表倍数所在位置的乘积
                        dp[i] += dp[j] * dp[index[right]]
                        # dp[i]与MOD取余
                        dp[i] %= MOD
        # 把dp表全加起来就是答案，按要求返回它与模数取余的结果                
        return sum(dp) % MOD
    # 最后，我还是没看懂这个算法到底特么是个什么道理
    # 为什么增加另两个位置的计数的乘积再取个余就是正确答案？
    