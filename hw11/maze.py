from disks import Disks


class Maze:
    """Draws the maze and handles interaction between disks"""
    def __init__(self, WIDTH, HEIGHT,
                 game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.gc = game_controller
        self.disks = Disks(self.WIDTH, self.HEIGHT)
        self.turn = 'black'

    def change_color(self, row, col):
        self.disks.change_color(row, col)

    def check_if_valid(self, color):
        '''Checks if there is any place that player can put disk in '''
        for i in range(len(self.disks.disks_lst)):
            for j in range(len(self.disks.disks_lst[0])):
                if self.disks.disks_lst[i][j] == 0 and self.disks.is_valid(color, i, j):
                    break
        if i == len(self.disks.disks_lst) and j == len(self.disks.disks_lst[0]):
            return False
        return True

    def update(self, color):
        if self.disks.white_count + self.disks.black_count == \
            len(self.disks.disks_lst) * len(self.disks.disks_lst[0]) or \
                not self.check_if_valid(color):
            if self.disks.white_count > self.disks.black_count:
                self.gc.player_white_wins = True
            else:
                self.gc.player_black_wins = True

    def display(self):
        self.update('white')
        self.disks.display()
        for i in range(0, self.WIDTH + 1, 100):
            strokeWeight(3)
            line(0, i, self.HEIGHT, i)
        for i in range(0, self.HEIGHT + 1, 100):
            strokeWeight(3)
            line(i, 0, i, self.WIDTH)
            
    def add_disk(self, x, y):
        if self.turn == 'black':
            self.disks.add_disk('black', x, y)
            self.disks.flip(self.turn, x//100, y//100)
            self.turn = 'white'
        else:
            self.disks.add_disk('white', x, y)
            self.disks.flip(self.turn, x//100, y//100)
            self.turn = 'black'
        self.update(self.turn)
        self.gc.update()

