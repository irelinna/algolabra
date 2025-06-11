from sympy import mod_inverse
import secrets


# empty list for found primes
list_of_primes = []

# fill prime list with Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):

    global list_of_primes

    # make a boolean array where all values = True
    prime = [True for i in range(limit+1)]
    
    # starting from 2
    p = 2
    while (p * p <= limit):

        # if this is not changed, prime[p] is a prime
        if (prime[p] == True):

            # updating all multiples of p to False
            for i in range(p * p, limit+1, p):
                prime[i] = False

        # check for multiples of next number
        p += 1

    # add all found primes to list
    for p in range(2, limit+1):
        if prime[p]:
            list_of_primes.append(p)
    
    return list_of_primes


# Miller-Rabin primality test. n = prime candidate, k = number of rounds
def miller_rabin(n, k=8):
    # numbers less than 2 are not prime
    if n < 2:
        return False


    # write n-1 as 2^r*d, so divide (n-1) by 2 as many times as possible
    # for example if n = 561, n-1 = 560
    # 560/2=280  ->  280/2=140  ->  140/2=70 ->  70/2=35 (odd)
    # so, (n-1) = 2^4*35
    # n = 561, r = 4, d = 35

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)  # for above example if a = 2, x = 2^35 mod 561 = 263
        # if x = 1 or n-1, stop checking
        if x == 1 or x == n - 1:
            continue
        # square x up to r-1 times (so 3 times in the example)
        for _ in range(r - 1):
            # x^2 mod n
            x = pow(x, 2, n)
            #if x = n-1, n is a prime number, else a composite
            if x == n - 1:
                break
        else:
            # x != n-1, n is a composite
            return False
    # x == n-1, n is a prime
    return True


# generate some prime number
def generate_prime(keysize):
    prime_list = sieve_of_eratosthenes(500)
    while True:
        candidate = secrets.randbits(keysize)
        candidate |= (1 << (keysize - 1))    # ensure that the candidate has exactly 1024 bits by making the highest bit 1
        candidate |= 1      # make it odd, even numbers cannot be prime

        # check candidate against list_of_primes
        if any(candidate % p == 0 for p in prime_list):
            continue
        # if candidate is not divisible by any prime in list_of_primes, then check with Miller-Rabin
        if miller_rabin(candidate):
            return candidate


# key generation
def generate_keys(keysize):
    p = generate_prime(keysize // 2)
    q = generate_prime(keysize // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    #Fermat prime
    e = 65537

    if phi % e == 0:
        raise ValueError("e is not coprime with phi(n). Choose different primes.")

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))



def string_to_int(message: str) -> int:
    return int.from_bytes(message.encode('utf-8'), byteorder='big')


def int_to_string(message_int: int) -> str:
    byte_length = (message_int.bit_length() + 7) // 8
    return message_int.to_bytes(byte_length, byteorder='big').decode('utf-8')


def encrypt(message, public_key):
    message_int = string_to_int(message)
    e, n = public_key
    if message_int >= n:
        raise ValueError("Message is too long to encrypt. Use a shorter message or bigger key.")
    return pow(message_int, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    message_int = pow(ciphertext, d, n)
    return int_to_string(message_int)


