class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.game_over = False
        self.winner = 'No one'
        self.number = 0

    def update(self):
        """Carries out necessary actions if player wins"""
        if self.game_over:
            fill(255, 255, 0)
            textSize(50)
            text("GAME OVER", self.WIDTH/2 - 140, self.HEIGHT/2 - 50)
            text(self.winner + " Wins", self.WIDTH/2 - 140,
                 self.HEIGHT/2 + 50)
            textSize(40)
            text('Winner has ' + str(self.number) + ' tiles',
                 self.WIDTH/2 - 160, self.HEIGHT/2 + 150)
