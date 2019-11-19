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
        # if self.gc.self.player_white_wins or self.gc.self.player_black_wins:
            

    def add_disk(self, color, wid, hei):
        '''Add a disk to maze'''
        column = wid // 100
        row = hei // 100
        if self.disks_lst[row][column] != 0:
            return False
        self.disks_lst[row][column] = Disk(color, row, column)
        if color == 'black':
            self.black_count += 1
        else:
            self.white_count += 1
        return True

    def change_color(self, row, col):
        '''Changes color of a disk'''
        BLACK = 1

        if self.disks_lst[row][col] != 0:
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
        else:
            color = 1

        visited = set()

        for i in range(row - 1, -1, -1):
            if self.disks_lst[i][col] == 0:
                break
            if i == row - 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row - 1 and self.disks_lst[i][col].color == color:
                for j in range(row - 1, i, -1):
                    if (j, col) not in visited:
                        visited.add((j, col))
                        self.change_color(j, col)

        for i in range(row + 1, self.row):
            if self.disks_lst[i][col] == 0:
                break
            if i == row + 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row + 1 and self.disks_lst[i][col].color == color:
                for j in range(row + 1, i):
                    if (j, col) not in visited:
                        visited.add((j, col))
                        self.change_color(j, col)

        for j in range(col - 1, -1, -1):
            if self.disks_lst[row][j] == 0:
                break
            if j == col - 1 and self.disks_lst[row][j].color == color:
                break
            elif self.disks_lst[row][j].color == color:
                for i in range(col - 1, j, -1):
                    if (row, i) not in visited:
                        visited.add((row, i))
                        self.change_color(row, i)

        for j in range(col + 1, self.column):
            if self.disks_lst[row][j] == 0:
                break
            if j == col + 1 and self.disks_lst[row][j].color == color:
                break
            elif self.disks_lst[row][j].color == color:
                for i in range(col + 1, self.column):
                    if (row, i) not in visited:
                        visited.add((row, i))
                        self.change_color(row, i)

        i = 1
        while row + i < self.row and col + i < self.column:
            if self.disks_lst[row + i][col + i] == 0:
                break
            if self.disks_lst[row + i][col + i].color == color:
                for k in range(1, i):
                    if (row + i, col + i) not in visited:
                        visited.add((row + i, col + i))
                        self.change_color(row + i, col + i)
                break
            i += 1

        i = 1
        while row - i >= 0 and col - i >= 0:
            if self.disks_lst[row - i][col - i] == 0:
                break
            if self.disks_lst[row - i][col - i].color == color:
                for k in range(1, i):
                    if (row - i, col - i) not in visited:
                        visited.add((row - i, col - i))
                        self.change_color(row - i, col - i)
                break
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == 0:
                break
            if self.disks_lst[row + i][col - i].color == color:
                for k in range(1, i):
                    if (row + i, col - i) not in visited:
                        visited.add((row + i, col - i))
                        self.change_color(row + i, col - i)
                break
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == 0:
                break
            if self.disks_lst[row + i][col - i].color == color:
                for k in range(1, i):
                    if (row + i, col - i) not in visited:
                        visited.add((row + i, col - i))
                        self.change_color(row + i, col - i)
                break
            i += 1

        i = 1
        while row - i >= 0 and col + i < self.column:
            if self.disks_lst[row - i][col + i] == 0:
                break
            if self.disks_lst[row - i][col + i].color == color:
                for k in range(1, i):
                    if (row - i, col + i) not in visited:
                        visited.add((row - i, col + i))
                        self.change_color(row - i, col + i)
                break
            i += 1

        if not visited:
            return False
        else:
            return True

    def is_valid(self, color, row, col):
        '''Check if player can put disk'''
        if color == 'white':
            color = 255
        else:
            color = 1
        for i in range(row - 1, -1, -1):
            if self.disks_lst[i][col] == 0:
                break
            if i == row - 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row - 1 and self.disks_lst[i][col].color == color:
                return True

        for i in range(row + 1, self.row):
            if self.disks_lst[i][col] == 0:
                break
            if i == row + 1 and self.disks_lst[i][col].color == color:
                break
            elif i != row + 1 and self.disks_lst[i][col].color == color:
                return True

        for j in range(col - 1, -1, -1):
            if self.disks_lst[row][j] == 0:
                break
            if j == col - 1 and self.disks_lst[row][j].color == color:
                break
            elif j != col - 1 and self.disks_lst[row][j].color == color:
                return True

        for j in range(col + 1, self.column):
            if self.disks_lst[row][j] == 0:
                break
            if j == col + 1 and self.disks_lst[row][j].color == color:
                break
            elif self.disks_lst[row][j].color == color:
                return True

        i = 1
        while row + i < self.row and col + i < self.column:
            if self.disks_lst[row + i][col + i] == 0:
                break
            if i == 1 and self.disks_lst[row + i][col + i].color == color:
                break
            if i >= 2 and self.disks_lst[row + i][col + i].color == color:
                return True
            i += 1

        i = 1
        while row - i >= 0 and col - i >= 0:
            if self.disks_lst[row - i][col - i] == 0:
                break
            if i == 1 and self.disks_lst[row - i][col - i].color == color:
                break
            if i >= 2 and self.disks_lst[row - i][col - i].color == color:
                return True
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == 0:
                break
            if i == 1 and self.disks_lst[row + i][col - i].color == color:
                break
            if i >= 2 and self.disks_lst[row + i][col - i].color == color:
                return True
            i += 1

        i = 1
        while row + i < self.row and col - i >= 0:
            if self.disks_lst[row + i][col - i] == 0:
                break
            if i == 1 and self.disks_lst[row + i][col - i].color == color:
                break
            if i >= 2 and self.disks_lst[row + i][col - i].color == color:
                return True
            i += 1

        i = 1
        while row - i >= 0 and col + i < self.column:
            if self.disks_lst[row - i][col + i] == 0:
                break
            if i == 1 and self.disks_lst[row - i][col + i].color == color:
                break
            if i >= 2 and self.disks_lst[row - i][col + i].color == color:
                return True
            i += 1

        return False
