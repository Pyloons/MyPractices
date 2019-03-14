'''
Typical Maze Solution
'''
class Maze:
    '''
    Define a maze with a rat
    '''
    def __init__(self, maze):
        self.wall_len = len(maze)
        self.has_walked = set()

    def print_solution(self, sol):
        '''
        print out solution
        '''
        i = 0

        while i < self.wall_len:
            j = 0

            while j < self.wall_len:
                print(sol[i][j], end='')
                j += 1
            print()
            i += 1

    def is_safe(self, maze, x_axis, y_axis):
        '''
        is safe
        '''
        comp_chain = [
            x_axis >= 0,
            x_axis < self.wall_len,
            y_axis >= 0,
            y_axis < self.wall_len,
            (x_axis, y_axis) not in self.has_walked
        ]
            
        return all(comp_chain) and maze[x_axis][y_axis] == 1

    def get_path(self, maze, x_axis, y_axis, sol):
        '''
        Find a path if has
        '''
        if x_axis == self.wall_len - 1 and y_axis == self.wall_len - 1:
            sol[x_axis][y_axis] = 1
            return True

        if self.is_safe(maze, x_axis, y_axis):
            self.has_walked.add((x_axis, y_axis))
            sol[x_axis][y_axis] = 1

            if self.get_path(maze, x_axis - 1, y_axis, sol):
                return True

            if self.get_path(maze, x_axis, y_axis - 1, sol):
                return True

            if self.get_path(maze, x_axis + 1, y_axis, sol):
                return True

            if self.get_path(maze, x_axis, y_axis + 1, sol):
                return True

            self.has_walked.remove((x_axis, y_axis))
            sol[x_axis][y_axis] = 0
            return False

        return False

if __name__ == "__main__":
    MAZE = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1]
    ]
    RAT = Maze(MAZE)
    SOL = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    if not RAT.get_path(MAZE, 0, 0, SOL):
        print('No Way')
        RAT.print_solution(SOL)
        RAT.print_solution(MAZE)
    else:
        RAT.print_solution(SOL)
