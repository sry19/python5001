from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    '''Test eat dots'''
    g = GameController(600, 600)
    m = Maze(600, 600, 150, 450,
             150, 450, g)
    start_count = len(m.dots.bottom_row)
    m.eat_dots(225, 450)
    m.eat_dots(300, 450)
    m.eat_dots(400, 460)
    end_count = len(m.dots.bottom_row)
    assert start_count - end_count == 3

    start_count = len(m.dots.top_row)
    m.eat_dots(225, 150)
    m.eat_dots(300, 150)
    m.eat_dots(376, 151)
    end_count = len(m.dots.top_row)
    assert start_count - end_count == 3

    start_count = len(m.dots.left_col)
    m.eat_dots(150, 410)
    m.eat_dots(150, 151)
    end_count = len(m.dots.left_col)
    assert start_count - end_count == 3

    start_count = len(m.dots.right_col)
    m.eat_dots(450, 410)
    m.eat_dots(450, 151)
    end_count = len(m.dots.right_col)
    assert start_count - end_count == 3
