from maze import Maze
from game_controller import GameController


def test_constructor():
    gc = GameController(400, 8)
    mz = Maze(400, 8, gc)
    assert mz.WIDTH == 400
    assert mz.grid_num == 8
    assert mz.side == 50
    assert mz.gc == gc
    assert mz.disks.row == 8
    assert mz.turn == 'black'


def test_change_color():
    gc = GameController(400, 8)
    mz = Maze(400, 8, gc)
    mz.change_color(3, 3)
    assert mz.disks.disks_lst[3][3].color == 1


def test_check_if_valid():
    gc = GameController(400, 2)
    mz = Maze(400, 2, gc)
    assert mz.check_if_valid('white') is False

    gc = GameController(400, 4)
    mz = Maze(400, 4, gc)
    assert mz.check_if_valid('white') is True


def test_update():
    gc = GameController(400, 2)
    mz = Maze(400, 2, gc)
    mz.update()
    assert gc.tie is True
    assert gc.number == 2
    assert gc.game_over is True


def test_add_disk():
    gc = GameController(400, 8)
    mz = Maze(400, 8, gc)
    mz.add_disk(4, 5)
    assert mz.disks.disks_lst[4][4].color == 1
    assert mz.turn == 'white'

    gc = GameController(400, 8)
    mz = Maze(400, 8, gc)
    mz.add_disk(3, 5)
    assert mz.turn == 'black'


def test_add_disk_ai():
    gc = GameController(400, 8)
    mz = Maze(400, 8, gc)
    mz.add_disk(4, 5)
    mz.add_disk_ai()
    assert mz.turn == 'black'

    gc = GameController(400, 8)
    mz = Maze(400, 8, gc)
    mz.add_disk_ai()
    assert mz.turn == 'black'
