from disks import Disks


class Maze:
    """Draws the board and handles interaction between disks"""
    def __init__(self, WIDTH, HEIGHT,
                 game_controller):
        '''Constructs a board'''
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.gc = game_controller
        self.disks = Disks(self.WIDTH, self.HEIGHT, game_controller)
        self.turn = 'black'

    def update(self):
        '''updates the state of the game'''
        if self.disks.white_count + self.disks.black_count == \
           len(self.disks.disks_lst) * len(self.disks.disks_lst[0]):
            self.gc.game_over = True
            if self.disks.white_count > self.disks.black_count:
                self.gc.winner = 'White'
                self.gc.number = self.disks.white_count
            elif self.disks.black_count > self.disks.white_count:
                self.gc.winner = 'Black'
                self.gc.number = self.disks.black_count
            else:
                self.gc.winner = 'No one'
                self.gc.number = self.disks.black_count
            self.turn = 0
            self.gc.update()

    def display(self):
        '''displays the board and tiles'''
        WIDTH = 100
        STROKE_WEI = 3

        self.update()
        self.disks.display()
        for i in range(0, self.WIDTH + 1, WIDTH):
            strokeWeight(STROKE_WEI)
            line(0, i, self.HEIGHT, i)
        for i in range(0, self.HEIGHT + 1, WIDTH):
            strokeWeight(STROKE_WEI)
            line(i, 0, i, self.WIDTH)

    def add_disk(self, x, y):
        '''Adds a tile to the board'''
        if self.turn != 'black' and self.turn != 'white':
            return
        if self.disks.add_disk(self.turn, y, x):
            if self.turn == 'black':
                self.turn = 'white'
            elif self.turn == 'white':
                self.turn = 'black'
        self.update()
        self.gc.update()
