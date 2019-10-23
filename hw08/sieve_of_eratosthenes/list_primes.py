# Author: Ruoyun Sun
# lists prime numbers from 2 to the argument value
from prime_generator import PrimeGenerator
import time
N = 1000000


def main():
    pg = PrimeGenerator()
    start = time.time()
    print(pg.primes_to_max(N))
    end = time.time()
    running_time = end - start
    print('time cost : %.5f sec' % running_time)


main()
