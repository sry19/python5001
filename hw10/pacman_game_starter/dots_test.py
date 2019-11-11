from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    ds = Dots(600, 600, 150, 450, 150, 450)
    start_count = len(ds.top_row)
    ds.eat(225, 150)
    ds.eat(300, 150)
    ds.eat(376, 151)
    end_count = len(ds.top_row)
    assert start_count - end_count == 3

    start_count = len(ds.bottom_row)
    ds.eat(225, 450)
    ds.eat(300, 450)
    ds.eat(400, 460)
    end_count = len(ds.bottom_row)
    assert start_count - end_count == 3

    ds = Dots(600, 600, 150, 450, 150, 450)
    start_count = len(ds.left_col)
    ds.eat(150, 410)
    ds.eat(150, 151)
    end_count = len(ds.left_col)
    assert start_count - end_count == 3

    start_count = len(ds.right_col)
    ds.eat(450, 410)
    ds.eat(450, 151)
    end_count = len(ds.right_col)
    assert start_count - end_count == 3


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
