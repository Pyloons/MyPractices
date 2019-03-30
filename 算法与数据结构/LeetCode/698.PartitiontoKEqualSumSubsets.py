'''
698. Partition to K Equal Sum Subsets
Medium

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

class OfficialSolution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: 'int') -> 'bool':
        # divmod是一个不常用的内置函数，同时返回两参数的整除结果和取余结果
        # 如果nums的总和不能被k整除，那么一定不会有合理的子集的
        target, rem = divmod(sum(nums), k)
        if rem:
            return False
        
        # 因为这道题时间复杂度很高，所以先排个序根本算不了什么
        nums.sort()
        
        # 如果nums里最大的值比整除出来的结果还大，也是不会有结果的
        # 毕竟这个数自己单独分一组也还是太大了
        if nums[-1] > target:
            return False
        
        # 如果最大值跟目标值一样，那这个值就可以单独分一组
        # 不再考虑它的细节，抛弃掉
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        
        # 由最下调用可知，groups是从长为k的0元素列表开始递归的
        def search(groups):
            print(groups)
            # 如果进入这个递归函数之前nums已经被折腾空了
            # 那么nums一定是可分的
            # 这是个递归思想，基线条件就是nums为空
            if not nums:
                return True
            
            # 取出最后一个值
            v = nums.pop()
            
            # 这个循环的目的在于不断地使用当前层的nums里的最大值往groups里填
            # 只要能填进去就为真，填不进去，说明至少会有一个组合比目标值大，所以不用继续循环了
            for i, group in enumerate(groups):
                # 如果这个从groups里取出来的值与刚取出来的最后一个值相加不大于目标平均值
                if group + v <= target:
                    # 那就让这个位置加v
                    groups[i] += v
                    # 把现在这个groups扔到下一层递归去，如果最终返回真，那么就跟着返回真
                    if search(groups):
                        return True
                    # 如果上面两行没有返回真，那就给它减回去，groups回滚到上一个状态
                    groups[i] -= v
                # 如果group为0
                if not group:
                    break
            # 上面的循环如果不能得到满足条件的结果，那就把v放回去，返回一个假
            nums.append(v)
            return False
            
        return search([0] * k)
                    