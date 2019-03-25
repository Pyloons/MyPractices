'''
973. K Closest Points to Origin - Medium

We have a list of points on the plane.
Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.
The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]

Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''

class MySortSolution:
    '''
    时间花费：444ms
    '''
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        def cal_dist(node):
            return node[0]**2 + node[1]**2
        
        dists = [cal_dist(x) for x in points]
        # 毫无意义，复习时重写
        sorted_dists = sorted(dists)
        max = sorted_dists[K-1]
        result = []
        for node in points:
            if len(result) >= K:
                break
            if cal_dist(node) <= max:
                result.append(node)
        return result

class OfficalSortSolution(object):
    '''
    目前最快算法就是这个，但是理论上第二个官方答案才应该更快
    时间花费：288ms
    思路跟我一样，内置排序……这根本就不是练习排序，而是练习sort方法key关键字参数的用法
    '''
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

import random


class OfficalDCSolution(object):
    '''
    分而治之算法，官方说时间复杂度是N
    稍微看了一下，核心算法仍然是快速排序，但是使用了类似二分查找的分而治之方法
    (快速排序就妙在这里，完全可以做到一边排序一边查找)
    每经过一轮快速排序，判断本次的pivot与K的大小关系，
    如果pivot大了，就只在左边进一步快排
    如果K大了，就只在右边进一步快排（反正此时左边的所有元素都要）
    注：只是粗略分析，可能有不对的地方
    '''
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
