from disks import Disks


class Maze:
    """Draws the maze and handles interaction between disks"""
    def __init__(self, WIDTH, HEIGHT,
                 game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.gc = game_controller
        self.disks = Disks(self.WIDTH, self.HEIGHT, game_controller)
        self.turn = 'black'

    def update(self):
        if self.disks.white_count + self.disks.black_count == \
           len(self.disks.disks_lst) * len(self.disks.disks_lst[0]):
            self.gc.game_over = True
            self.turn = 0
            self.gc.update()

    def display(self):
        self.update()
        self.disks.display()
        for i in range(0, self.WIDTH + 1, 100):
            strokeWeight(3)
            line(0, i, self.HEIGHT, i)
        for i in range(0, self.HEIGHT + 1, 100):
            strokeWeight(3)
            line(i, 0, i, self.WIDTH)

    def add_disk(self, x, y):
        if self.turn != 'black' and self.turn != 'white':
            return
        if self.disks.add_disk(self.turn, y//100, x//100):
            if self.turn == 'black':
                self.turn = 'white'
            elif self.turn == 'white':
                self.turn = 'black'
        self.update()
        self.gc.update()
