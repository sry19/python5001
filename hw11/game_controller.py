class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player_white_wins = False
        self.pinky_black_wins = False

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.player_white_wins:
            fill(1)
            textSize(50)
            text("WHITE WINS", self.WIDTH/2 - 140, self.HEIGHT/2)
        if self.pinky_black_wins:
            fill(1)
            textSize(50)
            text("BLACK WINS", self.WIDTH/2 - 140, self.HEIGHT/2)
