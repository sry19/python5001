from disk import Disk

START_TILE = 2
GRID_LENGTH = 100
INITIAL_VAL = 0


class Disks:
    '''A collection of disks'''
    def __init__(self, WIDTH, HEIGHT, gamecontroller):
        '''Contructs disks'''
        self.gc = gamecontroller
        self.width = WIDTH
        self.height = HEIGHT
        self.row = self.height // GRID_LENGTH
        self.column = self.width // GRID_LENGTH
        self.white_count = START_TILE
        self.black_count = START_TILE
        self.disks_lst = [[0 for _ in range(self.column)]
                          for _ in range(self.row)]
        self.disks_lst[self.row//2-1][self.column//2-1] = Disk('white',
                                                               self.row//2 - 1,
                                                               self.column//2-1
                                                               )
        self.disks_lst[self.row//2][self.column//2] = Disk('white',
                                                           self.row//2,
                                                           self.column//2
                                                           )
        self.disks_lst[self.row//2-1][self.column//2] = Disk('black',
                                                             self.row//2 - 1,
                                                             self.column//2
                                                             )
        self.disks_lst[self.row//2][self.column//2-1] = Disk('black',
                                                             self.row//2,
                                                             self.column//2 - 1
                                                             )

    def display(self):
        """Calls each disks's display method"""
        for i in range(self.row):
            for j in range(self.column):
                if self.disks_lst[i][j] != INITIAL_VAL:
                    self.disks_lst[i][j].display()

    def add_disk(self, color, row, column):
        '''Add a disk to maze'''
        if self.disks_lst[row][column] != INITIAL_VAL:
            return False
        self.disks_lst[row][column] = Disk(color, row, column)
        if color == 'black':
            self.black_count += 1
        elif color == 'white':
            self.white_count += 1
        return True
