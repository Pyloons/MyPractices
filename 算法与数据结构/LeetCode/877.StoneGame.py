'''
877. Stone Game
Medium

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
'''

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 只要先拿的人永远都只拿两头最大的，先拿永远赢
        # 这是最弱智的一道题了
        # return True
    
        # 动态规划也能做
        from functools import lru_cache
        
        N = len(piles)
        
        # 不限量缓存
        @lru_cache(None)
        def dp(i, j):
            # 由调用可知i,j是两个指针
            if i > j:
                return 0
            # 由于石头堆开始是偶数个，Alex又是先拿
            # 所以剩余偶数个时必定是Alex拿，奇数反之
            # 但是由于下面这个公式自身的问题，parity为1的时候才是Alex的回合
            parity = (j-i-N)%2
            if parity == 1:
                # Alex在两种拿法中取获利最大的
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i, j-1))
            else:
                # Lee在两种方法中取获利最小的
                return min(-piles[i]+ dp(i+1,j),-piles[j] + dp(i, j-1))
            # 最后注明一下，之所以在上面的递归中，总是让Lee拿去获利最小
            # 并不是因为人家在玩这个游戏的时候就是那么傻
            # 而是先手永远可以主动制定策略，使后手无法获得最大的分数
            # 这也是为什么直接返回True也能对的原因
            # 所以Lee的回合永远取min是这个道理
            # 因为不论是max还是min，起主导作用的都是Alex
        return dp(0, N-1) > 0
