from frequencies import NgramFrequencies


def test_add_item():
    nf = NgramFrequencies()
    word = ''
    nf.add_item(word)
    assert nf.n_gram_dict == {}
    assert nf.total_val == 0

    word = 'apple'
    nf.add_item(word)
    assert nf.n_gram_dict[word] == 1
    assert nf.total_val == 1

    word = 'apple'
    nf.add_item(word)
    assert nf.n_gram_dict[word] == 2
    assert nf.total_val == 2

    word = 'orange'
    nf.add_item(word)
    assert nf.n_gram_dict[word] == 1
    assert nf.total_val == 3


def test_top_n_counts():
    nf = NgramFrequencies()
    nf.add_item('apple')
    nf.add_item('apple')
    nf.add_item('apple')
    nf.add_item('orange')
    nf.add_item('grape')
    nf.add_item('meat')
    nf.add_item('orange')
    assert nf.top_n_counts(3) == [('apple', 3), ('orange', 2), ('grape', 1)]


def test_top_n_freqs():
    nf = NgramFrequencies()
    nf.add_item('apple')
    nf.add_item('apple')
    nf.add_item('apple')
    nf.add_item('orange')
    nf.add_item('grape')
    nf.add_item('meat')
    nf.add_item('orange')
    assert nf.top_n_freqs(3) == [('apple', 0.429), ('orange', 0.286),
                                 ('grape', 0.143)]


def test_frequency():
    nf = NgramFrequencies()
    nf.add_item('apple')
    nf.add_item('apple')
    nf.add_item('apple')
    nf.add_item('orange')
    nf.add_item('grape')
    nf.add_item('meat')
    nf.add_item('orange')
    assert nf.frequency('apple') == 0.429
    assert nf.frequency('orange') == 0.286
    assert nf.frequency('grape') == 0.143
