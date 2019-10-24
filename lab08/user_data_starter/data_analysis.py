import re


class DataAnalysis:
    '''A class representing DataAnalysis'''
    def __init__(self, file):
        '''constructs DataAnalysis object'''
        self.lang_dict = {}
        self.lang_total = 0
        self.country_dict = {}
        self.read_data(file)

    def read_data(self, file_name):
        '''read the data and get the counts'''
        try:
            f = open(file_name)
        except FileNotFoundError:
            print(file_name, 'is not found')
            return
        self.count_data(f)

    def count_data(self, f):
        '''counts language and 2-letter country top-level domain signifier'''
        line = f.readline().strip().split(',')
        lang_idx = line.index('language')
        country_idx = line.index('email')
        for line in f:
            language = line.strip().split(',')[lang_idx]
            email = line.split(',')[country_idx]
            country = re.findall(r"\.([a-z][a-z])$", email)
            for i in country:
                self.country_dict[i] = self.country_dict.get(i, 0) + 1
            self.lang_dict[language] = self.lang_dict.get(language, 0) + 1
            self.lang_total += 1

    def top_n_lang_freqs(self, n):
        '''takes a number N as an argument and return
           top n language frequencies
           int --> list'''
        for k, v in self.lang_dict.items():
            self.lang_dict[k] = v / self.lang_total
        return sorted(self.lang_dict.items(), key=lambda x: x[1],
                      reverse=True)[:n]

    def top_n_country_tlds_freqs(self, n):
        '''take a number N as an argument and return
            top n country top-level domain identifiers
            int --> list'''
        for k, v in self.country_dict.items():
            self.country_dict[k] = v / self.lang_total
        return sorted(self.country_dict.items(), key=lambda x: x[1],
                      reverse=True)[:n]
