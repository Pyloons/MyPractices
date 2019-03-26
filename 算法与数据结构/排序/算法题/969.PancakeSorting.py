'''
969. Pancake Sorting - Medium

Given an array A, we can perform a pancake flip: 
We choose some positive integer k <= A.length, 
then reverse the order of the first k elements of A.
We want to perform zero or more pancake flips 
(doing them one after another in succession) to sort the array A.
Return the k-values corresponding to a sequence of pancake flips that sort A.
Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 

Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
'''

'''
本题并没有做出来，故查看了教程
Solution
Approach 1: Sort Largest to Smallest
Intuition

We can place the largest element (in location i, 1-indexed) by flipping i to move the element to the first position,
then A.length to move it to the last position.
Afterwards, the largest element is in the correct position,
so we no longer need to pancake-flip by A.length or more.
We can repeat this process until the array is sorted.
Each move will use 2 flips per element.

Algorithm

First, sort the locations from largest value of A to smallest value of A.
For each element (from largest to smallest) with location i,
we will first simulate where this element actually is,
based on the pancake flips we have done. For a pancake flip f,
if i <= f, then the element has moved from location i to f+1 - i.
After, we flip by i then N-- to put this element in the correct position.

Complexity Analysis

Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(N). 
'''

'''
官方答案我不太懂它为什么要这么写，
因为它的描述是与最快答案相符合的，
与它自己所写的并不相符。
'''
class OfficalSolution(object):
    def pancakeSort(self, A):
        ans = []

        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1

        return ans

'''
但是仔细比对最快答案，其思路与我的类似，但是它利用了一个我没看到的条件，所以才成功了
'''

class FastestCommunitySolution(object):
    def pancakeSort(self, A: 'List[int]') -> 'List[int]':
        out = []
        # 这里不仅仅是获取A的长度，同时也是获取A中的最大值
        searchee = len(A)
        #find searchee
        while(searchee > 1):
            # 这里就是我没有看到的条件，详见Note 2
            # 由于searchee的双重身份，所以可以用来求得最大值的位置
            searchee_idx = A.index(searchee)
            if searchee_idx == 0:
                # 如果[最大值searchee]出现在第一个位置，
                # 那么就全部逆序，
                # 然后把[长度searchee]加入out
                A[:searchee] = A[:searchee][::-1]
                out.append(searchee)
            else:
                # 如果[最大值searchee]并没有出现在第一个位置
                # 那就从它出现的位置开始，向前所有元素逆序
                # 把逆序的数量传入out
                A[:searchee_idx+1] = A[:searchee_idx+1][::-1]
                out.append(searchee_idx + 1)
                # 再来个全逆序，并把逆序的数量传入out
                A[:searchee] = A[:searchee][::-1]
                out.append(searchee)
            # 每经过一步，该步骤的最大值的位置已经尘埃落定，
            # 应该不考虑这个值，然后开始下一个了
            searchee -= 1
        return out


class MyFaultSolution(object):
    def pancakeSort(self, A: 'List[int]') -> 'List[int]':

        if len(A) <= 1:
            return []
        
        a = A[:]
        result = []
        n = len(a)
        done = False
        while not done:
            if a[0] > a[-1]:
                a = a[::-1]
                result.append(n)
            else:
                flag = a[0] < a[1]
                if flag:
                    change = False
                    for i in range(n-1):
                        if a[i] > a[i+1]:
                            result.append(i+1)
                            a = a[0:i+1][::-1] + a[i+1:]
                            change = True
                            break
                    if not change:
                        done = True
                else:
                    for i in range(n-1):
                        if a[i] < a[i+1]:
                            result.append(i+1)
                            a = a[0:i+1][::-1] + a[i+1:]
                            break
        return result
    