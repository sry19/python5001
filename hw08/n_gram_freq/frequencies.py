

class NgramFrequencies:
    def __init__(self):
        self.n_gram_dict = {}
        self.total_val = 0

    def add_item(self, n_gram):
        if n_gram == '':
            return
        if n_gram in self.n_gram_dict:
            self.n_gram_dict[n_gram] += 1
        else:
            self.n_gram_dict[n_gram] = 1
        self.total_val += 1

    def top_n_counts(self, n):
        return sorted(self.n_gram_dict.items(),
                      key=lambda x: x[1],
                      reverse=True)[:n]

    def top_n_freqs(self, n):
        for k, v in self.n_gram_dict.items():
            self.n_gram_dict[k] = self.frequency(k)
        return sorted(self.n_gram_dict.items(),
                      key=lambda x: x[1],
                      reverse=True)[:n]

    def frequency(self, n_gram):
        return round(self.n_gram_dict[n_gram]/self.total_val, 3)
