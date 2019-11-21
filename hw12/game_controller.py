YELLOW = (255, 255, 0)
BIG_WORD = 50
SMALL_WORD = 40


class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, GRID_NUM):
        self.WIDTH = WIDTH
        self.grid_num = GRID_NUM
        if GRID_NUM == 0:
            self.side_length = 0
        else:
            self.side_length = self.WIDTH // self.grid_num
        self.player_white_wins = False
        self.player_black_wins = False
        self.tie = False
        self.number = 0
        self.game_over = False
        self.once = True
        self.records = []

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.player_white_wins:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("WHITE WINS", self.WIDTH/2 - 140, self.WIDTH/2)
            textSize(SMALL_WORD)
            text('Winner has ' + str(self.number) + ' tiles',
                 self.WIDTH/2 - 170, self.WIDTH/2 + 150)

        elif self.player_black_wins:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("BLACK WINS", self.WIDTH/2 - 140, self.WIDTH/2)
            textSize(SMALL_WORD)
            text('Winner has ' + str(self.number) + ' tiles',
                 self.WIDTH/2 - 170, self.WIDTH/2 + 150)

        elif self.tie:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("TIE", self.WIDTH/2 - 140, self.WIDTH/2)

    def setup(self):
        if self.player_black_wins:
            answer = self.input('enter your name')
        elif self.player_white_wins:
            answer = 'computer'
        if answer:
            print('hi ' + answer)
        elif answer == '':
            print('[empty string]')
        else:
            print(answer)  # Canceled dialog will print None
        self.lst_add(answer, self.number)

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def lst_add(self, answer, number):
        '''Add new record and sort'''

        f = open('scores.txt', 'r')
        if f:
            for line in f:
                if not line or line.isspace():
                    continue
                line = line.strip()
                idx = line.rfind(' ')
                ans, num = line[:idx], line[idx+1:]
                self.records.append([ans, num])

        f = open('scores.txt', 'w')
        if not self.records:
            self.records.append([answer, number])
        else:
            if number > int(self.records[0][1]):
                self.records.insert(0, [answer, number])
            else:
                self.records.append([answer, number])

        for ans, num in self.records:
            if not ans:
                continue
            f.write(str(ans) + ' ' + str(num)+'\n')
