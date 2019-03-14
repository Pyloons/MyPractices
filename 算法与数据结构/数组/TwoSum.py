'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = ,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        length = len(nums)
        while i < length - 1:
            if j >= length:
                i += 1
                j = i + 1
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        return None


'''
这个解答有点hash表的意思
用原始案例来演示一下：
1 buf={}, nums = [2, 7, 11, 15], target = 9
2 buf={7:0}, nums = [2, 7, 11, 15], target = 9
3 buf={7:0}, nums = [2, 7, 11, 15], target = 9 return [0, 1]
它的实质是：把每一个nums中的元素，想凑出target，需要加上的数作为字典的Key与该元素的下标绑定，
如果之后遇到某个元素的值，在buf中当Key，那么被绑到Key上的下标与这个元素的下标就正好可以凑成答案。
这个答案的时间复杂度是O(n)，我的是O(nlogn)惭愧了；关键在于我没有充分利用target这个参数。

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
'''

