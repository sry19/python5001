YELLOW = (255, 255, 0)
BIG_WORD = 50
SMALL_WORD = 40


class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, GRID_NUM):
        self.WIDTH = WIDTH
        self.grid_num = GRID_NUM
        self.side_length = self.WIDTH / self.grid_num
        self.player_white_wins = False
        self.player_black_wins = False
        self.tie = False
        self.number = 0

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.player_white_wins:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("WHITE WINS", self.WIDTH/2 - 140, self.WIDTH/2)
            textSize(SMALL_WORD)
            text('Winner has ' + str(self.number) + ' tiles',
                 self.WIDTH/2 - 170, self.WIDTH/2 + 150)
        if self.player_black_wins:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("BLACK WINS", self.WIDTH/2 - 140, self.WIDTH/2)
            textSize(SMALL_WORD)
            text('Winner has ' + str(self.number) + ' tiles',
                 self.WIDTH/2 - 170, self.WIDTH/2 + 150)
        if self.tie:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("TIE", self.WIDTH/2 - 140, self.WIDTH/2)
