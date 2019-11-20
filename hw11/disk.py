class Disk:
    '''A disk'''
    def __init__(self, color, row, column):
        if color == 'white':
            self.color = 255
        elif color == 'black':
            self.color = 1
        self.row = row
        self.column = column

    def display(self):
        '''Draws the disk'''
        DIAMETER = 90
        POSITION = 50
        SIDE_LENGTH = 100

        fill(self.color)
        ellipse(self.column * SIDE_LENGTH + POSITION,
                self.row * SIDE_LENGTH + POSITION,
                DIAMETER, DIAMETER)
