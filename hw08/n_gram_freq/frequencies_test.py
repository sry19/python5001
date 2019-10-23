from frequencies import NgramFrequencies


def test_add_item():
    nf = NgramFrequencies()
    word = ''
    nf.add_item(word)
    assert nf.n_gram_dict == {}
    assert nf.total_val = 0

    word = 'apple'
    nf.add_item(word)
    assert nf.n_gram_dict[word] == 1
    assert nf.total_val = 1

    word = 'apple'
    nf.add_item(word)
    assert nf.n_gram_dict[word] == 2
    assert nf.total_val = 2

    word = 'orange'
    nf.add_item(word)
    assert nf.n_gram_dict[word] == 1
    assert nf.total_val = 3


def test_top_n_counts():
    pass


def test_top_n_freqs():
    pass


def test_frequency():
    pass
