from disk import Disk

INITIAL_COUNT = 2
INITIAL_VAL = 0


class Disks:
    '''A collection of disks'''
    def __init__(self, WIDTH, gamecontroller):
        self.gc = gamecontroller
        self.width = WIDTH
        self.row = self.width // self.gc.side_length
        self.column = self.width // self.gc.side_length
        self.white_count = INITIAL_COUNT
        self.black_count = INITIAL_COUNT
        self.disks_lst = [[0 for _ in range(self.column)]
                          for _ in range(self.row)]
        self.disks_lst[self.row//2-1][self.column//2-1] = Disk('white',
                                                               self.row//2 - 1,
                                                               self.column // 2
                                                               - 1,
                                                               self.gc
                                                               )
        self.disks_lst[self.row//2][self.column//2] = Disk('white',
                                                           self.row//2,
                                                           self.column//2,
                                                           self.gc
                                                           )
        self.disks_lst[self.row//2-1][self.column//2] = Disk('black',
                                                             self.row//2 - 1,
                                                             self.column//2,
                                                             self.gc
                                                             )
        self.disks_lst[self.row//2][self.column//2-1] = Disk('black',
                                                             self.row//2,
                                                             self.column // 2
                                                             - 1,
                                                             self.gc
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
        self.disks_lst[row][column] = Disk(color, row, column, self.gc)
        if color == 'black':
            self.black_count += 1
        elif color == 'white':
            self.white_count += 1
        return True

    def change_color(self, row, col):
        '''Changes color of a disk'''
        BLACK = 1

        if self.disks_lst[row][col] != INITIAL_VAL:
            self.disks_lst[row][col].change_color()
            if self.disks_lst[row][col].color == BLACK:
                self.black_count += 1
                self.white_count -= 1
            else:
                self.black_count -= 1
                self.white_count += 1

    def flip(self, color, row, col):
        '''flips the disks'''
        if color == 'white':
            color = 255
        elif color == 'black':
            color = 1

        visited = set()

        for i in range(row - 1, -1, -1):
            if self.disks_lst[i][col] == INITIAL_VAL:
                break
            if i == row - 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row - 1 and self.disks_lst[i][col].color == color:
                for j in range(row - 1, i, -1):
                    if (j, col) not in visited:
                        visited.add((j, col))
                break

        for i in range(row + 1, self.row):
            if self.disks_lst[i][col] == INITIAL_VAL:
                break
            if i == row + 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row + 1 and self.disks_lst[i][col].color == color:
                for j in range(row + 1, i):
                    if (j, col) not in visited:
                        visited.add((j, col))
                break

        for j in range(col - 1, -1, -1):
            if self.disks_lst[row][j] == INITIAL_VAL:
                break
            if j == col - 1 and self.disks_lst[row][j].color == color:
                break
            elif j != col - 1 and self.disks_lst[row][j].color == color:
                for i in range(col - 1, j, -1):
                    if (row, i) not in visited:
                        visited.add((row, i))
                break

        for j in range(col + 1, self.column):
            if self.disks_lst[row][j] == INITIAL_VAL:
                break
            if j == col + 1 and self.disks_lst[row][j].color == color:
                break
            elif self.disks_lst[row][j].color == color:
                for i in range(col + 1, j):
                    if (row, i) not in visited:
                        visited.add((row, i))
                break

        i = 1
        while row + i < self.row and col + i < self.column:
            if self.disks_lst[row + i][col + i] == INITIAL_VAL:
                break
            if self.disks_lst[row + i][col + i].color == color:
                for k in range(1, i):
                    if (row + k, col + k) not in visited:
                        visited.add((row + k, col + k))
                break
            i += 1

        i = 1
        while row - i >= 0 and col - i >= 0:
            if self.disks_lst[row - i][col - i] == INITIAL_VAL:
                break
            if self.disks_lst[row - i][col - i].color == color:
                for k in range(1, i):
                    if (row - k, col - k) not in visited:
                        visited.add((row - k, col - k))
                break
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == INITIAL_VAL:
                break
            if self.disks_lst[row + 1][col - 1].color == color:
                break
            if self.disks_lst[row + i][col - i].color == color:
                for k in range(1, i):
                    if (row + k, col - k) not in visited:
                        visited.add((row + k, col - k))
                break
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == INITIAL_VAL:
                break
            if self.disks_lst[row + i][col - i].color == color:
                for k in range(1, i):
                    if (row + k, col - k) not in visited:
                        visited.add((row + k, col - k))
                break
            i += 1

        i = 1
        while row - i >= 0 and col + i < self.column:
            if self.disks_lst[row - i][col + i] == INITIAL_VAL:
                break
            if self.disks_lst[row - 1][col + 1].color == color:
                break
            if self.disks_lst[row - i][col + i].color == color:
                for k in range(1, i):
                    if (row - k, col + k) not in visited:
                        visited.add((row - k, col + k))
                break
            i += 1
        visited = list(visited)
        for i, j in visited:
            self.change_color(i, j)

    def is_valid(self, color, row, col):
        '''Check if player can put disk'''
        if self.disks_lst[row][col] != INITIAL_VAL:
            return False

        if color == 'white':
            color = 255
        elif color == 'black':
            color = 1

        for i in range(row - 1, -1, -1):
            if self.disks_lst[i][col] == INITIAL_VAL:
                break
            if i == row - 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row - 1 and self.disks_lst[i][col].color == color:
                return True

        for i in range(row + 1, self.row):
            if self.disks_lst[i][col] == INITIAL_VAL:
                break
            if i == row + 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row + 1 and self.disks_lst[i][col].color == color:
                return True

        for j in range(col - 1, -1, -1):
            if self.disks_lst[row][j] == INITIAL_VAL:
                break
            if j == col - 1 and self.disks_lst[row][j].color == color:
                break
            elif j != col - 1 and self.disks_lst[row][j].color == color:
                return True

        for j in range(col + 1, self.column):
            if self.disks_lst[row][j] == INITIAL_VAL:
                break
            if j == col + 1 and self.disks_lst[row][j].color == color:
                break
            elif j != col + 1 and self.disks_lst[row][j].color == color:
                return True

        i = 1
        while row + i < self.row and col + i < self.column:
            if self.disks_lst[row + i][col + i] == INITIAL_VAL:
                break
            if i == 1 and self.disks_lst[row + i][col + i].color == color:
                break
            if i >= 2 and self.disks_lst[row + i][col + i].color == color:
                return True
            i += 1

        i = 1
        while row - i >= 0 and col - i >= 0:
            if self.disks_lst[row - i][col - i] == INITIAL_VAL:
                break
            if i == 1 and self.disks_lst[row - i][col - i].color == color:
                break
            if i >= 2 and self.disks_lst[row - i][col - i].color == color:
                return True
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == INITIAL_VAL:
                break
            if i == 1 and self.disks_lst[row + i][col - i].color == color:
                break
            if i >= 2 and self.disks_lst[row + i][col - i].color == color:
                return True
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == INITIAL_VAL:
                break
            if i == 1 and self.disks_lst[row + i][col - i].color == color:
                break
            if i >= 2 and self.disks_lst[row + i][col - i].color == color:
                return True
            i += 1

        i = 1
        while row - i >= 0 and col + i < self.column:
            if self.disks_lst[row - i][col + i] == INITIAL_VAL:
                break
            if i == 1 and self.disks_lst[row - i][col + i].color == color:
                break
            if i >= 2 and self.disks_lst[row - i][col + i].color == color:
                return True
            i += 1

        return False
