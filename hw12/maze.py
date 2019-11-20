from disks import Disks


class Maze:
    """Draws the maze and handles interaction between disks"""
    def __init__(self, WIDTH, GRID_NUM,
                 game_controller):
        self.WIDTH = WIDTH
        self.grid_num = GRID_NUM
        self.side = self.WIDTH / self.grid_num
        self.gc = game_controller
        self.disks = Disks(self.WIDTH, game_controller)
        self.turn = 'black'

    def change_color(self, row, col):
        '''change the color of a disk'''
        self.disks.change_color(row, col)

    def check_if_valid(self, color):
        '''Checks if there is any place that player can put disk in '''
        flag = False
        for i in range(len(self.disks.disks_lst)):
            for j in range(len(self.disks.disks_lst[0])):
                if self.disks.disks_lst[i][j] == 0 and \
                   self.disks.is_valid(color, i, j):
                    flag = True
                    break
        return flag

    def update(self):
        '''updates the state of the game'''
        if self.disks.white_count + self.disks.black_count == \
            len(self.disks.disks_lst) * len(self.disks.disks_lst[0]) or \
                not self.check_if_valid(self.turn):
            if self.disks.white_count > self.disks.black_count:
                self.gc.player_white_wins = True
            else:
                self.gc.player_black_wins = True
            self.turn = 0
            self.gc.update()

    def display(self):
        '''displays maze and disks'''
        STROKE_WEI = 3

        self.update()
        self.disks.display()
        for i in range(0, self.WIDTH + 1, self.side):
            strokeWeight(STROKE_WEI)
            line(0, i, self.WIDTH, i)
        for i in range(0, self.WIDTH + 1, self.side):
            strokeWeight(STROKE_WEI)
            line(i, 0, i, self.WIDTH)

    def add_disk(self, x, y):
        '''adds disks to the board'''
        if self.turn != 'black' and self.turn != 'white':
            return
        if not self.disks.is_valid(self.turn, y, x):
            return
        if self.turn == 'black':
            self.disks.add_disk('black', y, x)
            self.disks.flip(self.turn, y, x)
            self.turn = 'white'
        elif self.turn == 'white':
            self.disks.add_disk('white', y, x)
            self.disks.flip(self.turn, y, x)
            self.turn = 'black'
        self.update()
        self.gc.update()
