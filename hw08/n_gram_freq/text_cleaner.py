import re
from frequencies import NgramFrequencies
N = 10


class TextCleaner:
    def __init__(self):
        self.word_lst = []
        self.nf_uni = NgramFrequencies()
        self.nf_bi = NgramFrequencies()
        self.nf_tri = NgramFrequencies()

    def pre_process(self, file_content):
        # file_content = re.sub(r"[A-Z][a-z]\.", '', file_content,
        #                       count=0, flags=0)
        file_content = re.sub("Dr.", "Dr", file_content,
                              count=0, flags=0)
        file_content = re.sub("Mr.", "Mr", file_content,
                              count=0, flags=0)
        return file_content

    def separate_sentences(self, file_content):
        file_content = re.sub(r"[()[\]{}:\-\"]", '', file_content,
                              count=0, flags=0)
        new_content = file_content.rstrip().lower().replace(',', ' COMMA')
        file_content_lst = new_content.split(' ')
        for i in file_content_lst:
            if i == '':
                file_content_lst.remove(i)
        self.word_lst.append(file_content_lst)

    def count_uni_word(self):
        for word_lst in self.word_lst:
            for word in word_lst:
                self.nf_uni.add_item(word)
        print("Top", N, "unigrams:")
        for pair in self.nf_uni.top_n_freqs(N):
            print("  ", pair)

    def count_bi_word(self):
        for word_lst in self.word_lst:
            for idx in range(len(word_lst)-1):
                self.nf_bi.add_item(word_lst[idx] + '_' + word_lst[idx + 1])
        print("Top", N, "bigrams:")
        for pair in self.nf_bi.top_n_freqs(N):
            print("  ", pair)

    def count_tri_word(self):
        for word_lst in self.word_lst:
            for idx in range(len(word_lst) - 2):
                self.nf_tri.add_item(word_lst[idx] + '_'
                                     + word_lst[idx + 1]
                                     + '_' + word_lst[idx + 2])
        print("Top", N, "trigrams:")
        for pair in self.nf_tri.top_n_freqs(N):
            print("  ", pair)
