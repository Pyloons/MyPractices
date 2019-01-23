import curses
from random import randrange, choice
from collections import defaultdict

class Prefab(object):
    actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
    def __init__(self):
        pass

    @staticmethod
    def get_actions():
        return Prefab.actions


class StateMachine(object):
    def __init__(self, stdscr):
        
        curses.use_default_colors()

        self.stdscr = stdscr
        self.game_field = GameField(win=2048)
        self.state_actions = {
            'Init': self.init,
            'Win': lambda: self.game_end('Win'),
            'Gameover': lambda: self.game_end('Gameover'),
            'Game': self.gaming
        }
        
        self.state = 'Init'
        while self.state != 'Exit':
            self.state = self.state_actions[self.state]()

    def init(self):
        self.game_field.reset()
        return 'Game'

    def game_end(self, state):
        self.game_field.draw(self.stdscr)
        action = self.get_user_action(self.stdscr)

        response = defaultdict(lambda: state)
        response['Restart'], response['Exit'] = 'Init', 'Exit'
        return response[action]

    def gaming(self):
        self.game_field.draw(self.stdscr)
        action = self.get_user_action(self.stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if self.game_field.move(action):
            if self.game_field.is_win():
                return 'Win'
            if self.game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    def get_user_action(self, keyboard):
        char = 'N'
        letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
        actions_dict = dict(zip(letter_codes, Prefab.get_actions() * 2))
        while char not in actions_dict:
            char = keyboard.getch()
        return actions_dict[char]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()

    def transpose(self, field):
        return [list(row) for row in zip(*field)]

    def invert(self, field):
        return [row[::-1] for row in field]

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
            def tighten(row):
                new_row = [i for i in row if i != 0]
                zero_count = range(len(row) - len(new_row))
                new_row += [0 for i in zero_count]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
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

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: self.invert(moves['Left'](self.invert(field)))
        moves['Up'] = lambda field: self.transpose(moves['Left'](self.transpose(field)))
        moves['Down'] = lambda field: self.transpose(moves['Right'](self.transpose(field)))

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
        return not any(self.move_is_possible(move) for move in Prefab.get_actions())

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](self.invert(field))
        check['Up'] = lambda field: check['Left'](self.transpose(field))
        check['Down'] = lambda field: check['Right'](self.transpose(field))

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
    curses.wrapper(StateMachine)
