'''
为了应付Pylint，做了一点不太好看的修改
'''
import curses
from random import randrange, choice
from collections import defaultdict


actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes, actions * 2))



def main(stdscr):
    '''
    正经入口函数，接受一个标准屏幕的变量做参数
    三个子函数init、game_end、gaming（不同状态如何处理）
    与curses的wrapper函数（类似按帧检查更新状态）
    将main函数变成真正的状态机
    '''

    # 不明原理不好说该不该放在这里
    curses.use_default_colors()  # 一般来说应该放到外面去

    game_field = GameField(win=2048)
    state = 'Init'

    def init():
        game_field.reset()
        return 'Game'

    def game_end(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        response = defaultdict(lambda: state)
        response['Restart'], response['Exit'] = 'Init', 'Exit'
        return response[action]

    def gaming():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: game_end('Win'),
        'Gameover': lambda: game_end('Gameover'),
        'Game': gaming
       }

    while state != 'Exit':
        state = state_actions[state]()


def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


def transpose(field):
    '''
    接受一个二维数组field
        zip函数接受zip(*iter)这样的形式，
        表示先把iter每一个元素拆成一个又一个单独的子list，
        然后集体将其zip，即将每一个子list的同位元素挨个打包
        这与直接zip(iter)所得到的无用结果差别很大
    zip(*field)可以实现这个二维数组的转置操作
    list(row)把转置后的每一行从tuple变成list
    返回该转置矩阵
    '''
    return [list(row) for row in zip(*field)]


def invert(field):
    '''
    接受一个二维数组field
    返回每一行都左右逆置后的二维数组
    '''
    return [row[::-1] for row in field]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        ir = range(self.width)
        jr = range(self.height)
        cl = [(i, j) for i in ir for j in jr if self.field[i][j] == 0]
        (i, j) = choice(cl)
        self.field[i][j] = new_element

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        ir = range(self.width)
        jr = range(self.height)
        self.field = [[0 for i in ir] for j in jr]
        self.spawn()
        self.spawn()

    def move(self, direction):
        def move_row_left(row):
            '''
            接受一个list，对其进行往左2048式融合
            '''
            def tighten(row):
                '''
                接受一个list对象，进行紧缩操作
                原理：
                首先生成一个新数组，这个数组是传入数组去掉0的结果
                然后往新数组里填充传入list与新list长度差额数量的0
                这样就完成了紧缩
                '''
                new_row = [i for i in row if i != 0]
                zero_count = range(len(row) - len(new_row))
                new_row += [0 for i in zero_count]
                return new_row

            def merge(row):
                '''
                接受一个list，进行融合操作（往左融合）
                原理：
                首先，设置一个成对标记(默认False)和一个空的新list
                然后开始遍历检查传入的原list
                    1.如果成双对，那么新list添加一个该位置元素两倍
                    的值，并把标记设为假;
                    2.如果没有成双对
                        a.如果当前不是最后一个元素并且当前元素与后
                        一个元素相等，那么标记置True，新list添加0
                        b.如果当前是最后一个元素，或者与后面不等，
                        那么新list添加当前元素
                最后返回一个先紧缩，再融合，再紧缩的结果
                例如:
                    输入：[0,0,2,2]
                    紧缩：[0,0,2,2] => [2,2] => [2,2,0,0]
                    融合：[2,2,0,0] => [0,4,0,0]
                    紧缩：[0,4,0,0] => [4,0,0,0]
                '''
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]  # 这是个计分的操作
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            return tighten(merge(tighten(row)))

        '''
        先毫不废话，通过转置和镜像的方法，
        准备好能产生四个方向上按一下的结果的匿名函数（其实并不匿名）
        如果方向标识在moves字典中的话，就判断能不能移动
        如果能,
            取该方向上的匿名函数算出下一步的结果，
            通过赋值更新当前的field,
            生成一个新2或4，并返回真
        如果不能，返回假
        先点个赞，这个字典写的很骚气我很喜欢;
        我想吐槽的两点是
            第一这个moves并不需要放在这里，不然每动一次都要生成一次moves
            第二如果不用赋值的方式而是直接定义字典，那么可能不会收到pylint的抱怨
        '''
        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                '''元素i等于0，而且它右边那个不为0'''
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                '''元素i不等于0，而且它右边那个跟它是一对'''
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        '''
        这个check字典跟上面的moves差不多，点赞与吐槽并存
        '''
        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '(R)Restart (Q)Exit'
        gameover_string = 'YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))

        for row in self.field:
            draw_hor_separator()
            draw_row(row)

        draw_hor_separator()

        if self.is_win():
            cast(gameover_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)


if __name__ == '__main__':
    '''
    入口，是curses的最典型用法
    '''
    curses.wrapper(main)
