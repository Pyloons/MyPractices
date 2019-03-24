'''
922. Sort Array By Parity II
Easy

225

22

Favorite

Share
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

'''

# 自我评价：
# 思路与最快答案是一样的
# 最快答案写得更加简洁直白
# 时间有差距应该是常数差距

# 我的答案 152ms
class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        is_even_search = True
        even_side_wrong = False
        odd_side_wrong = False
        n = len(A)
        even_idx = 0
        odd_idx = 1
        while even_idx < n and odd_idx <= n - 1:
            # print(even_idx, odd_idx, A)
            if even_side_wrong and odd_side_wrong:
                A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
                even_side_wrong = False
                even_idx += 2
                odd_side_wrong = False
                odd_idx += 2
            if even_idx < n and odd_idx <= n - 1:
                if is_even_search:
                    if A[even_idx] % 2 == 0:
                        even_idx += 2
                    else:
                        even_side_wrong = True
                        is_even_search = False
                else:
                    if A[odd_idx] % 2 == 1:
                        odd_idx += 2
                    else:
                        odd_side_wrong = True
                        is_even_search = True
        return A

# 最快答案 116ms
class Solution_Fastest:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        j = 1
        for i in range(0, len(A), 2):
            if(A[i] % 2):
                while(A[j]%2):
                    j+=2
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        return A
   
class Solution_Two_Pass(object):
    '''
    新建一个等长数组，并按条件插入
    时空复杂度都是n
    '''
    def sortArrayByParityII(self, A):
        N = len(A)
        ans = [None] * N

        t = 0
        # 这里和下面的循环都没必要用枚举，因为根本没用上
        for i, x in enumerate(A):
            if x % 2 == 0:
                ans[t] = x
                t += 2

        t = 1
        for i, x in enumerate(A):
            if x % 2 == 1:
                ans[t] = x
                t += 2

        # We could have also used slice assignment:
        # ans[::2] = (x for x in A if x % 2 == 0)
        # ans[1::2] = (x for x in A if x % 2 == 1)

        return ans


class Solution_RW_Heads(object):
    '''
    官方版最佳答案，与最快答案的区别仅仅在于交换数值比较Pythonic
    '''
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
