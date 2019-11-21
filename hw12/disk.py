BLACK = 1
WHITE = 255


class Disk:
    '''A disk'''
    def __init__(self, color, row, column, gamecontroller):
        if color == 'white':
            self.color = WHITE
        elif color == 'black':
            self.color = BLACK
        self.row = row
        self.column = column
        self.gc = gamecontroller

    def display(self):
        '''Draws the disk'''
        fill(self.color)
        ellipse(self.column * self.gc.side_length + 0.5 * self.gc.side_length,
                self.row * self.gc.side_length + 0.5 * self.gc.side_length,
                0.9 * self.gc.side_length,
                0.9 * self.gc.side_length)

    def change_color(self):
        '''Changes color of a disk'''
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE
        self.display()
