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

