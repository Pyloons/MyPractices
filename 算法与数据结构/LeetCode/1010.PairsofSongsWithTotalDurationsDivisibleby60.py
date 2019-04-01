'''
1010. Pairs of Songs With Total Durations Divisible by 60
Easy

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
'''
# 我并不是很懂这个算法
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        needs = [0] * 60
        
        for i in time:
            needs[i%60] += 1
        # 经过上述循环，time中每个元素与60取余的结果
        # 都化为了needs的下标，而needs中的每个数，都是与time取余的结果出现的次数
        for i in range(0,31):
            # 这个余数没有出现过，不管
            if needs[i] == 0:
                continue
            # 余数为0或30的时间，同时这个余数出现过
            if i == 0 or i == 30:
                if needs[i] > 1:
                    # 这样计数
                    count += (needs[i]*(needs[i]-1)//2)
            # 如果余数不是0或30
            else:
                # 这样计数
                count+=(needs[i]*needs[60-i])
        return count