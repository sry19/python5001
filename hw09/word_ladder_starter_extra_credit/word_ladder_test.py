from word_ladder_extra_point import WordLadder


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words


def test_constructor():
    '''Test __init__'''
    valid_words = load_words()
    w1, w2 = "earth", "ocean"
    wl = WordLadder(w1, w2, valid_words)
    assert wl.start_word == "earth"
    assert wl.end_word == "ocean"
    assert wl.word_set == valid_words


def test_make_ladder():
    '''Test make_ladder'''
    valid_words = load_words()
    w1, w2 = "a", "apple"
    wl = WordLadder(w1, w2, valid_words)
    assert wl.make_ladder().items == ["a", "al", "apl", "appl", "apple"]

    w1, w2 = "love", "hat"
    wl = WordLadder(w1, w2, valid_words)
    assert wl.make_ladder().items == ["love", "loe", "hoe", "hae", "hat"]
