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
        self.bool_lst = [True] * (num + 1)
        self.bool_lst[0] = False
        self.bool_lst[1] = False
        # reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        for i in range(2, int(num**0.5)+1):
            if self.bool_lst[i]:
                for j in range(i*i, num+1, i):
                    self.compos_set.add(j)
                    self.bool_lst[j] = False
        for i in range(2, num+1):
            if self.bool_lst[i]:
                self.prime_lst.append(i)
        return self.prime_lst
