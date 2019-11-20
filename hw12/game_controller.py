class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, GRID_NUM):
        self.WIDTH = WIDTH
        self.grid_num = GRID_NUM
        self.side_length = self.WIDTH / self.grid_num
        self.player_white_wins = False
        self.player_black_wins = False

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.player_white_wins:
            fill(1)
            textSize(50)
            text("WHITE WINS", self.WIDTH/2 - 140, self.WIDTH/2)
        if self.player_black_wins:
            fill(1)
            textSize(50)
            text("BLACK WINS", self.WIDTH/2 - 140, self.WIDTH/2)
