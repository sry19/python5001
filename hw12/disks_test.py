from disks import Disks
from game_controller import GameController
from disk import Disk


def test_constructor():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    assert dks.gc == gc
    assert dks.width == 400
    assert dks.row == 8
    assert dks.column == 8
    assert dks.white_count == 2
    assert dks.black_count == 2
    assert dks.disks_lst[3][3].color == 255
    assert dks.disks_lst[4][4].color == 255
    assert dks.disks_lst[3][4].color == 1
    assert dks.disks_lst[4][3].color == 1

    gc = GameController(400, 2)
    dks = Disks(400, gc)
    assert dks.disks_lst[0][0].color == 255
    assert dks.disks_lst[0][1].color == 1
    assert dks.disks_lst[1][0].color == 1
    assert dks.disks_lst[1][1].color == 255

    gc = GameController(400, 0)
    dks = Disks(400, gc)
    assert dks.disks_lst == []


def test_add_disk():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    assert dks.add_disk('white', 3, 4) is False
    assert dks.add_disk('black', 0, 1) is True


def test_change_color():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    dks.change_color(3, 4)
    dks.change_color(0, 0)
    assert dks.disks_lst[3][4].color == 255
    assert dks.disks_lst[0][0] == 0


def test_flip():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    dks.disks_lst[4][5] = Disk('black', 4, 5, gc)
    dks.flip('black', 4, 5)
    assert dks.disks_lst[4][4].color == 1


def test_is_valid():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    dks.disks_lst[4][5] = Disk('black', 4, 5, gc)
    dks.flip('black', 4, 5)
    assert dks.is_valid('white', 3, 5) is True
    assert dks.is_valid('white', 3, 6) is False


def test_computer_ai():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    dks.disks_lst[4][5] = Disk('black', 4, 5, gc)
    dks.flip('black', 4, 5)
    dks.disks_lst[5][3] = Disk('white', 5, 3, gc)
    dks.flip('white', 5, 3)
    assert dks.computer_ai() == (3, 5)


def test_choose_best_pos():
    gc = GameController(400, 8)
    dks = Disks(400, gc)
    dks.disks_lst[4][5] = Disk('black', 4, 5, gc)
    dks.flip('black', 4, 5)
    dks.disks_lst[5][3] = Disk('white', 5, 3, gc)
    dks.flip('white', 5, 3)
    assert dks.choose_best_pos(3, 5) == {(3, 4), (4, 4)}
