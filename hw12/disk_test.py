from disk import Disk
from game_controller import GameController


def test_constructor():
    gc = GameController(400, 8)
    dk = Disk('white', 1, 3, gc)
    assert dk.color == 255
    assert dk.row == 1
    assert dk.column == 3
    assert dk.gc == gc


def test_change_color():
    gc = GameController(400, 8)
    dk = Disk('white', 1, 3, gc)
    dk.change_color()
    assert dk.color == 1
