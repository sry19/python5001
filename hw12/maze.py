from disks import Disks

COLOR_BLACK = 'black'
COLOR_WHITE = 'white'
INITIAL_VAL = 0
YELLOW = (255, 255, 0)
FONT_WORD = 25


class Maze:
    """Draws the maze and handles interaction between disks"""
    def __init__(self, WIDTH, GRID_NUM,
                 game_controller):
        self.WIDTH = WIDTH
        self.grid_num = GRID_NUM
        if GRID_NUM == 0:
            self.side = 0
        else:
            self.side = self.WIDTH / self.grid_num
        self.gc = game_controller
        self.disks = Disks(self.WIDTH, game_controller)
        self.turn = COLOR_BLACK

    def change_color(self, row, col):
        '''change the color of a disk'''
        self.disks.change_color(row, col)

    def check_if_valid(self, color):
        '''Checks if there is any place that player can put disk in '''
        flag = False
        for i in range(len(self.disks.disks_lst)):
            for j in range(len(self.disks.disks_lst[0])):
                if self.disks.disks_lst[i][j] == INITIAL_VAL and \
                   self.disks.is_valid(color, i, j):
                    flag = True
                    break
        return flag

    def update(self):
        '''updates the state of the game'''
        if self.turn == 0:
            return
        if self.disks.white_count + self.disks.black_count == \
            len(self.disks.disks_lst) * len(self.disks.disks_lst[0]) or \
                (not self.check_if_valid(COLOR_BLACK) and
                 not self.check_if_valid(COLOR_WHITE)):
            if self.disks.white_count > self.disks.black_count:
                self.gc.player_white_wins = True
                self.gc.number = self.disks.white_count
            elif self.disks.white_count < self.disks.black_count:
                self.gc.player_black_wins = True
                self.gc.number = self.disks.black_count
            else:
                self.gc.tie = True
                self.gc.number = self.disks.white_count
            self.turn = 0
            self.gc.game_over = True
            self.gc.user_score = self.disks.black_count
        if not self.check_if_valid(COLOR_BLACK):
            self.turn = COLOR_WHITE
        elif not self.check_if_valid(COLOR_WHITE):
            self.turn = COLOR_BLACK

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
        if self.turn == COLOR_BLACK:
            fill(*YELLOW)
            textSize(FONT_WORD)
            text("PLAYER: BLACK", self.WIDTH/2 - 140, 25)
        if self.turn == COLOR_WHITE:
            fill(*YELLOW)
            textSize(FONT_WORD)
            text("PLAYER: WHITE", self.WIDTH/2 - 140, 25)

    def add_disk(self, x, y):
        '''adds disks to the board'''
        if self.turn != COLOR_BLACK:
            return
        if not self.disks.is_valid(self.turn, y, x):
            return
        self.disks.add_disk(self.turn, y, x)
        self.disks.flip(self.turn, y, x)
        self.turn = COLOR_WHITE

    def add_disk_ai(self):
        if self.turn != COLOR_WHITE:
            return
        if not self.check_if_valid(self.turn):
            return
        r, c = self.disks.computer_ai()
        self.disks.add_disk(self.turn, r, c)
        self.disks.flip(self.turn, r, c)
        self.turn = COLOR_BLACK
