from dot import Dot


class Dots:
    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    def eat(self, x, y):
        '''Eat every dot Pac-man meets'''
        if abs(self.TH - y) < self.EAT_DIST:
            for i in range(len(self.top_row) - 1, -1, -1):
                if abs(self.top_row[i].x - x) < self.EAT_DIST:
                    del self.top_row[i]
        elif abs(self.BH - y) < self.EAT_DIST:
            for i in range(len(self.bottom_row) - 1, -1, -1):
                if abs(self.bottom_row[i].x - x) < self.EAT_DIST:
                    del self.bottom_row[i]
        if abs(self.LV - x) < self.EAT_DIST:
            for i in range(len(self.left_col) - 1, -1, -1):
                if abs(self.left_col[i].y - y) < self.EAT_DIST:
                    del self.left_col[i]
        elif abs(self.RV - x) < self.EAT_DIST:
            for i in range(len(self.right_col) - 1, -1, -1):
                if abs(self.right_col[i].y - y) < self.EAT_DIST:
                    del self.right_col[i]

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))
