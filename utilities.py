import random

# generate some prime number
def generate_large_prime(keysize):
    while True:
        prime = random.getrandbits(keysize)
        if is_prime(prime):
            return prime

# check for prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# key generation
def generate_keys(keysize=1024):
    p = generate_large_prime(keysize // 2)
    q = generate_large_prime(keysize // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if phi % e == 0:
        raise ValueError("e is not coprime with phi(n). Choose different primes.")

    d = pow(e, -1, phi)
    return ((e, n), (d, n))


#TODO: encryption and decryption


