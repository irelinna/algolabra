import unittest 
from .. import utilities

class TestUtilities(unittest.TestCase):
    def test_int_string(self):
        message = "tarkistetaan"
        self.assertEqual(utilities.int_to_string(utilities.string_to_int(message)),message)

    def test_encrypt_decrypt(self):
        public_key, private_key = utilities.generate_keys(2048)
        original = "testi tekstiviesti"
        ciphertext = utilities.encrypt(original, public_key)
        decrypted = utilities.decrypt(ciphertext, private_key)
        # compare original and encrypted + decrypted message
        self.assertEqual(decrypted,original)

    def test_public_private(self):
        public_key, private_key = utilities.generate_keys(2048)
        e, n1 = public_key
        d, n2 = private_key
        self.assertEqual(n1,n2) # n should be the same
        self.assertNotEqual(e,d) # public and private exponents should differ

    def test_miller_rabin(self):
        # primes should return True, composites False
        self.assertEqual(utilities.miller_rabin(101),True)
        self.assertEqual(utilities.miller_rabin(561),False)
        self.assertEqual(utilities.miller_rabin(17),True)
        self.assertEqual(utilities.miller_rabin(100),False)

    def test_prime_generation(self):
        prime = utilities.generate_prime(2048)
        # check that bit length is correct
        self.assertGreaterEqual(prime.bit_length(),2048)
        # check that prime generation generates a prime
        self.assertEqual(utilities.miller_rabin(prime),True)
