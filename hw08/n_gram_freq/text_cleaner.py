import re
from frequencies import NgramFrequencies


class TextCleaner:
    def __init__(self):
        '''constructs the TextCleaner'''
        self.word_lst = []
        self.nf_uni = NgramFrequencies()
        self.nf_bi = NgramFrequencies()
        self.nf_tri = NgramFrequencies()

    def pre_process(self, file_content):
        '''pre-processes the string
            string --> string'''
        all_abb = set(re.findall(r"[A-Z][a-z]\.", file_content))
        for i in all_abb:
            file_content = re.sub(i, i[:-1], file_content,
                                  count=0, flags=0)
        return file_content

    def separate_sentences(self, file_content):
        '''generates word list
            string --> None'''
        file_content = re.sub(r"(\-)\s", ' ', file_content,
                              count=0, flags=0)
        new_content = file_content.strip().lower().replace(',', ' COMMA')
        file_content_lst = re.findall(r"[a-zA-Z]+[\'\-]?[a-zA-Z]*",
                                      new_content)
        if file_content_lst:
            self.word_lst.append(file_content_lst)

    def count_uni_word(self, n):
        '''counts unigrams'''
        for word_lst in self.word_lst:
            for word in word_lst:
                self.nf_uni.add_item(word)
        return self.nf_uni.top_n_freqs(n)

    def print_out_uni(self, n):
        '''prints top n unigrams'''
        print("Top", n, "unigrams:")
        for pair in self.count_uni_word(n):
            print("  ", pair)

    def count_bi_word(self, n):
        '''counts bigrams'''
        for word_lst in self.word_lst:
            for idx in range(len(word_lst) - 1):
                self.nf_bi.add_item(word_lst[idx] + '_' + word_lst[idx + 1])
        return self.nf_bi.top_n_freqs(n)

    def print_out_bi(self, n):
        '''prints top n bigrams'''
        print("Top", n, "bigrams:")
        for pair in self.count_bi_word(n):
            print("  ", pair)

    def count_tri_word(self, n):
        '''counts trigrams'''
        for word_lst in self.word_lst:
            for idx in range(len(word_lst) - 2):
                self.nf_tri.add_item(word_lst[idx] + '_'
                                     + word_lst[idx + 1]
                                     + '_' + word_lst[idx + 2])
        return self.nf_tri.top_n_freqs(n)

    def print_out_tri(self, n):
        '''prints top n trigrams'''
        print("Top", n, "trigrams:")
        for pair in self.count_tri_word(n):
            print("  ", pair)
