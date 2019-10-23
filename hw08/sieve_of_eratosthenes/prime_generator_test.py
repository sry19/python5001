from prime_generator import PrimeGenerator


def test_primes_to_max():
    pg = PrimeGenerator()
    assert 7919 in pg.primes_to_max(10000)
