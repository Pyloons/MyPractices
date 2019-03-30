'''
810. Chalkboard XOR Game
Hard

We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:

1 <= N <= 1000. 
0 <= nums[i] <= 2^16.
'''
class OfficialLikeSolution:
    def xorGame(self, nums: 'List[int]') -> 'bool':
        # from functools import reduce
        # 又学到一个reduce的用法，默认函数过于厉害了
        # return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
        
        def xor_all(num_list):
            result = 0
            for i in num_list:
                result ^= i
            return result
        
        # 如果擦掉一个数会导致剩下的数挨个异或后得0会让Alice输掉
        # 那么Bob一定会赢，反过来Alice也一样会赢
        # 这道题需要返回的是Alice是否有赢的可能，并不是问Alice如何赢，所以不必要回答怎么赢
        # 另一种情况就是经过异或计算后整个序列如果不为0
        # 那么当其长度为奇数时，先擦必输
        # 相对的，当其长度为偶数时，先擦必赢
        return xor_all(nums) == 0 or len(nums) % 2 == 0