from game_controller import GameController


def test_contructor():
    gc = GameController(400, 8)
    assert gc.WIDTH == 400
    assert gc.grid_num == 8
    assert gc.side_length == 50
    assert gc.player_white_wins is False
    assert gc.player_black_wins is False
    assert gc.tie is False
    assert gc.number == 0
    assert gc.game_over is False
    assert gc.once is True
    assert gc.records == []