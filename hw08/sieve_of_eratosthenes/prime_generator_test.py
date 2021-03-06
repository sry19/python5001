from prime_generator import PrimeGenerator


def test_constructor():
    '''tests __init__'''
    pg = PrimeGenerator()
    assert pg.compos_set == set()
    assert pg.prime_lst == []


def test_primes_to_max():
    '''tests primes_to_max'''
    pg = PrimeGenerator()
    assert 7919 in pg.primes_to_max(10000)
    assert 5701 in pg.primes_to_max(10000)
    assert 211 in pg.primes_to_max(211)
    assert 222 not in pg.primes_to_max(500)

    pg_2 = PrimeGenerator()
    pg_2.primes_to_max(500)
    assert 269 == pg_2.prime_lst[56]
    assert 419 == pg_2.prime_lst[80]
    assert 2 == pg_2.prime_lst[0]
    assert 73 == pg_2.prime_lst[20]
