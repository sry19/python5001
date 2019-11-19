class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.game_over = False

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.game_over:
            fill(1)
            textSize(50)
            text("GAME_OVER", self.WIDTH/2 - 140, self.HEIGHT/2)
