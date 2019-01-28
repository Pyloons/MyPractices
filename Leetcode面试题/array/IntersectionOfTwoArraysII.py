class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    result.append(i)
                    nums2.pop(nums2.index(i))
        else:
            for i in nums2:
                if i in nums1:
                    result.append(i)
                    nums1.pop(nums1.index(i))
        return result
        
'''
# 我觉得不错的一个高赞答案，易读、比我的内置函数用的少、效率还高……
class Solution(object):
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res
'''

'''
迁移到中国版之后发现的更好的一个版本，时间消耗是我的一半，还是字典大法
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        for num in nums1:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                dic[num] -= 1
                res.append(num)
        return res
'''

