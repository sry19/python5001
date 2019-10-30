from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    sp = StringProcessor()
    assert sp.process_string("ab") == ""
    assert sp.process_string("ab*") == "b"
    assert sp.process_string("ab^") == "ba"
    assert sp.process_string("^") == ""
