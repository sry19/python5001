from bracket_match import BracketMatch


def test_constructor():
    '''Test __init__'''
    bm = BracketMatch()
    assert bm.match_dict == {'(': ')', '[': ']', '{': '}'}


def test_brackets_match():
    """Test brackets_match method"""
    bm = BracketMatch()
    assert bm.brackets_match("()") is True
    assert bm.brackets_match("a(a[a])a({a})") is True
    assert bm.brackets_match("(") is False
    assert bm.brackets_match("(}") is False
    assert bm.brackets_match("a(a(a)a(a)") is False
    assert bm.brackets_match("aa(a))a(a)") is False
