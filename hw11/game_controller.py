YELLOW = (255, 255, 0)


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
        BIG_WORD = 50
        SMALL_WORD = 40

        if self.game_over:
            fill(*YELLOW)
            textSize(BIG_WORD)
            text("GAME OVER", self.WIDTH/2 - 140, self.HEIGHT/2 - 50)
            text(self.winner + " Wins", self.WIDTH/2 - 140,
                 self.HEIGHT/2 + 50)
            textSize(SMALL_WORD)
            text('Winner has ' + str(self.number) + ' tiles',
                 self.WIDTH/2 - 160, self.HEIGHT/2 + 150)
