class Solution(object):
    def __init__(self):
        self.has_walked = set()
        self.grid_width = None
        self.time = 0
        self.bfs = []
        
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid_width = len(grid)
        
        x_axis = 0
        y_axis = 0
        
        start_time = max(grid[self.grid_width-1][self.grid_width-1], grid[0][0])
        end_time = self.grid_width**2 - 1
        
        while start_time < end_time:
            self.time = (start_time + end_time) // 2
            self.has_walked = set()
            self.bfs = []
            # print('>', start_time,self.time,end_time)
            if self.has_path(grid, x_axis, y_axis):
                end_time = self.time
            else:
                start_time = self.time + 1
            # print(start_time,self.time,end_time,'>')
        return start_time
        
    def has_path(self, grid, x_axis, y_axis):
        # print(self.has_walked)
        self.bfs.append((0, 0))
        self.has_walked.add((0, 0))
        
        for x_axis, y_axis in self.bfs:
            if grid[x_axis][y_axis] <= self.time:#self.is_safe(grid, x_axis, y_axis):
                if self.time == 66:
                    print(self.time, grid[x_axis][y_axis],(x_axis,y_axis))

                if x_axis == self.grid_width - 1 and y_axis == self.grid_width - 1:
                    # if self.time == 66:
                    #     print([grid[x][y] for x,y in self.bfs],len(self.bfs),len(self.has_walked))
                    # print('Done')
                    return True
            
                if self.is_safe(grid, x_axis - 1, y_axis):
                    self.bfs.append((x_axis - 1, y_axis))
                    self.has_walked.add((x_axis - 1, y_axis))
                    if self.time == 66:
                        print(self.time,':',grid[x_axis][y_axis], 'go up to', grid[x_axis - 1][y_axis])
                    
                if self.is_safe(grid, x_axis + 1, y_axis):
                    self.bfs.append((x_axis + 1, y_axis))
                    self.has_walked.add((x_axis + 1, y_axis))
                    if self.time == 66:
                        print(self.time,':',grid[x_axis][y_axis], 'go down to', grid[x_axis + 1][y_axis])
                    
                if self.is_safe(grid, x_axis, y_axis - 1):
                    self.bfs.append((x_axis, y_axis - 1))
                    self.has_walked.add((x_axis, y_axis - 1))
                    if self.time == 66:
                        print(self.time,':',grid[x_axis][y_axis], 'go left to', grid[x_axis][y_axis - 1])
                    
                if self.is_safe(grid, x_axis, y_axis + 1):
                    self.bfs.append((x_axis, y_axis + 1))
                    self.has_walked.add((x_axis, y_axis + 1))
                    if self.time == 66:
                        print(self.time,':',grid[x_axis][y_axis], 'go right to', grid[x_axis][y_axis + 1])
                    
                # self.has_walked.remove((x_axis, y_axis))
                # return False
        
        return False
            
    
    def is_safe(self, grid, x_axis, y_axis):
        safe_checks = [
            x_axis >= 0,
            x_axis < self.grid_width,
            y_axis >= 0,
            y_axis < self.grid_width,
            (x_axis, y_axis) not in self.has_walked
        ]
        # if all(safe_checks):
            # print(self.has_walked,'check for', x_axis, y_axis, all(safe_checks))
            # print(self.has_walked,'check for', x_axis, y_axis, grid[x_axis][y_axis], self.time, grid[x_axis][y_axis] <= self.time)
        return all(safe_checks)# and grid[x_axis][y_axis] <= self.time

if __name__ == "__main__":
    a = Solution()
    grid = [
        [26,99,80,1,89,86,54,90,47,87],
        [9,59,61,49,14,55,77,3,83,79],
        [42,22,15,5,95,38,74,12,92,71],
        [58,40,64,62,24,85,30,6,96,52],
        [10,70,57,19,44,27,98,16,25,65],
        [13,0,76,32,29,45,28,69,53,41],
        [18,8,21,67,46,36,56,50,51,72],
        [39,78,48,63,68,91,34,4,11,31],
        [97,23,60,17,66,37,43,33,84,35],
        [75,88,82,20,7,73,2,94,93,81]]
    grid2 = [
        [31,28,33,0,8,57,86,99,23,98],
        [25,90,20,73,34,65,29,9,42,46],
        [17,84,10,4,40,5,41,21,71,79],
        [13,70,69,81,63,93,77,1,94,53],
        [38,87,61,50,92,2,15,95,82,68],
        [44,72,88,47,27,91,37,48,83,16],
        [3,30,96,66,7,58,76,54,19,64],
        [85,45,60,11,51,26,6,22,74,32],
        [43,12,62,59,89,52,36,97,49,78],
        [75,24,14,67,56,35,55,39,80,18]]
    import time
    start = time.time()
    print(a.swimInWater(grid2))
    print(time.time() - start)