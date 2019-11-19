from disk import Disk


class Disks:
    '''A collection of disks'''
    def __init__(self, WIDTH, HEIGHT, gamecontroller):
        self.gc = gamecontroller
        self.width = WIDTH
        self.height = HEIGHT
        self.row = self.height // 100
        self.column = self.width // 100
        self.white_count = 2
        self.black_count = 2
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
                if self.disks_lst[i][j] != 0:
                    self.disks_lst[i][j].display()

    def add_disk(self, color, row, column):
        '''Add a disk to maze'''
        if self.disks_lst[row][column] != 0:
            return False
        self.disks_lst[row][column] = Disk(color, row, column)
        if color == 'black':
            self.black_count += 1
        elif color == 'white':
            self.white_count += 1
        return True
