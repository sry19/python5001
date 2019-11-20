class Disk:
    '''A disk'''
    def __init__(self, color, row, column, gamecontroller):
        if color == 'white':
            self.color = 255
        elif color == 'black':
            self.color = 1
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
        if self.color == 255:
            self.color = 1
        else:
            self.color = 255
        self.display()
