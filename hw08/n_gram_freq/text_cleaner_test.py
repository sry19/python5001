from text_cleaner import TextCleaner


def test_constructor():
    '''tests __init__'''
    tc = TextCleaner()
    assert tc.word_lst == []
    assert tc.nf_uni.n_gram_dict == {}
    assert tc.nf_uni.total_val == 0
    assert tc.nf_bi.n_gram_dict == {}
    assert tc.nf_bi.total_val == 0
    assert tc.nf_tri.n_gram_dict == {}
    assert tc.nf_tri.total_val == 0


def test_pre_process():
    tc = TextCleaner()
    file_content = "Directed by Mr. Burton and Mike Johnson."
    assert tc.pre_process(file_content) == '''Directed by Mr Burton and Mi\
ke Johnson.'''


def test_separate_sentences():
    tc = TextCleaner()
    file_content = '''A necro- philiac entertainment for the whole family to e\
njoy, '''
    tc.separate_sentences(file_content)
    assert tc.word_lst == [['a', 'necro', 'philiac', 'entertainment', 'for',
                            'the', 'whole', 'family', 'to', 'enjoy', 'COMMA']]


def test_count_uni_word():
    tc = TextCleaner()
    file_content = '''A necro- philiac entertainment for the whole family to e\
njoy, '''
    tc.separate_sentences(file_content)
    assert tc.count_uni_word(3) == [('a', 0.091), ('necro', 0.091),
                                    ('philiac', 0.091)]
    assert tc.nf_uni.n_gram_dict == {'a': 0.091, 'necro': 0.091,
                                     'philiac': 0.091, 'entertainment': 0.091,
                                     'for': 0.091, 'the': 0.091,
                                     'whole': 0.091, 'family': 0.091,
                                     'to': 0.091, 'enjoy': 0.091,
                                     'COMMA': 0.091}
    assert tc.nf_uni.total_val == 11


def test_count_bi_word():
    tc = TextCleaner()
    file_content = '''A necro- philiac entertainment for the a necro family'''
    tc.separate_sentences(file_content)
    file_content = '''to enjoy, '''
    tc.separate_sentences(file_content)
    assert tc.count_bi_word(3) == [('a_necro', 0.2), ('necro_philiac', 0.1),
                                   ('philiac_entertainment', 0.1)]
    assert tc.nf_bi.n_gram_dict == {'a_necro': 0.2, 'necro_philiac': 0.1,
                                    'philiac_entertainment': 0.1,
                                    'entertainment_for': 0.1,
                                    'for_the': 0.1, 'the_a': 0.1,
                                    'necro_family': 0.1, 'to_enjoy': 0.1,
                                    'enjoy_COMMA': 0.1}
    assert tc.nf_bi.total_val == 10


def test_count_tri_word():
    tc = TextCleaner()
    file_content = '''A necro- philiac entertainment for the whole family to e\
njoy, '''
    tc.separate_sentences(file_content)
    assert tc.count_tri_word(3) == [('a_necro_philiac', 0.111),
                                    ('necro_philiac_entertainment', 0.111),
                                    ('philiac_entertainment_for', 0.111)]
    assert tc.nf_tri.n_gram_dict == {'a_necro_philiac': 0.111,
                                     'necro_philiac_entertainment': 0.111,
                                     'philiac_entertainment_for': 0.111,
                                     'entertainment_for_the': 0.111,
                                     'for_the_whole': 0.111,
                                     'the_whole_family': 0.111,
                                     'whole_family_to': 0.111,
                                     'family_to_enjoy': 0.111,
                                     'to_enjoy_COMMA': 0.111
                                     }
    assert tc.nf_tri.total_val == 9
