class Disk:
    '''A disk'''
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column

    def display(self):
        '''Draws the disk'''
        fill(self.color)
        ellipse(self.column * 100 + 50, self.row * 100 + 50, 90, 90)

    def change_color(self):
        '''Changes color of a disk'''
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
