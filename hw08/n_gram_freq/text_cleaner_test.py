from text_cleaner import TextCleaner


def test_pre_process():
    tc = TextCleaner()
    file_content = "Directed by Mr. Burton and Mike Johnson."
    assert tc.pre_process(file_content) == '''Directed by Mr Burton and Mi
ke Johnson.'''


def test_separate_sentences():
    tc = TextCleaner()
    file_content = '''A necro- philiac entertainment for the whole family to e
njoy, '''
    assert tc.separate_sentences(file_content) == '''a necro philiac enterta
inment for the whole family to enjoy COMMA'''
    tc.word_lst = [['a', 'necro', 'philiac', 'entertainment', 'for', 'the',
                    'whole', 'family', 'to', 'enjoy', 'COMMA']]


def test_count_uni_word():
    tc = TextCleaner()
    tc.word_lst = [['a', 'necro', 'philiac', 'entertainment', 'for', 'the',
                    'whole', 'family', 'to', 'enjoy', 'COMMA']]
    tc.count_uni_word()
    assert tc.nf_uni.n_gram_dict == {'a': 1, 'necro': 1, 'philiac': 1,
                                     'entertainment': 1, 'for': 1, 'the': 1,
                                     'whole': 1, 'family': 1, 'to': 1,
                                     'enjoy': 1, 'COMMA': 1}
    assert tc.nf_uni.total_val == 11


def test_count_bi_word():
    tc = TextCleaner()
    tc.word_lst = [['a', 'necro', 'philiac', 'entertainment', 'for', 'the',
                    'whole', 'family', 'to', 'enjoy', 'COMMA']]
    tc.count_bi_word()
    assert tc.nf_bi.n_gram_dict == {'a_necro': 1, 'necro_philiac': 1,
                                    'philiac_entertainment': 1,
                                    'entertainment_for': 1, 'for_the': 1,
                                    'the_whole': 1, 'whole_family': 1,
                                    'family_to': 1, 'to_enjoy': 1,
                                    'enjoy_COMMA': 1}
    assert tc.nf_bi.total_val == 10


def test_count_tri_word():
    tc = TextCleaner()
    tc.word_lst = [['a', 'necro', 'philiac', 'entertainment', 'for', 'the',
                    'whole', 'family', 'to', 'enjoy', 'COMMA']]
    tc.count_tri_word()
    assert tc.nf_tri.n_gram_dict == {'a_necro_philiac': 1,
                                     'necro_philiac_entertainment': 1,
                                     'philiac_entertainment_for': 1,
                                     'entertainment_for_the': 1,
                                     'for_the_whole': 1, 'the_whole_family': 1,
                                     'whole_family_to': 1,
                                     'family_to_enjoy': 1, 'to_enjoy_COMMA': 1
                                     }
    assert tc.nf_tri.total_val == 9
