# Author: Ruoyun Sun
# lists prime numbers from 2 to the argument value
from prime_generator import PrimeGenerator
N = 1000000


def main():
    pg = PrimeGenerator()
    print(pg.primes_to_max(N))


main()
