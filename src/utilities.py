import random
from sympy import randprime, mod_inverse

# generate some prime number
def generate_prime(keysize):
    return randprime(1,keysize)


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


