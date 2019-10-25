class PrimeGenerator:
    '''A class representing prime generator'''
    def __init__(self):
        '''constructs the object'''
        self.compos_set = set()
        self.prime_lst = []

    def primes_to_max(self, num):
        ''' takes an integer argument and returns a list of all primes from
             2 to the argument value
             PrimeGenerator object, integer -> list'''
        # reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        for i in range(2, int(num ** 0.5) + 1):
            if i not in self.compos_set:
                for j in range(i * i, num + 1, i):
                    self.compos_set.add(j)
        for i in range(2, num + 1):
            if i not in self.compos_set:
                self.prime_lst.append(i)
        return self.prime_lst
