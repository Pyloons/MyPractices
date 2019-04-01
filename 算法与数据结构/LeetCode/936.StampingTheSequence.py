'''
https://leetcode.com/articles/stamping-the-sequence/
这道题我并不理解，官解也非常长
'''

class OfficialSolution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)
        from collections import deque
        
        queue = deque()
        done = [False] * N
        ans = []
        A = []
        for i in range(N - M + 1):
            # 对于每个窗口[i, i+M)
            # A[i]有“哪些需要改变”的信息
            # 在我们在i处盖章之前
            
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i + j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))
            
            # 如果我们可以在i处立刻盖章
            # 从这个窗口将字母入队
            if not todo:
                ans.append(i)
                for j in range(i, i+len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True
                        
        # 对于每个入队的字母
        while queue:
            i = queue.popleft()
            
            # 对于每个有可能被影响的窗口
            # j: 窗口的起点
            for j in range(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]:  # 这个窗口被影响了
                    A[j][1].discard(i)  # 从这个窗口的todo中移除它
                    if not A[j][1]:
                        ans.append(j)
                        for m in A[j][0]:
                            if not done[m]:
                                queue.append(m)
                                done[m] = True
                                
        return ans[::-1] if all(done) else []
