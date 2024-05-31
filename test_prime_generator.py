import unittest
from main import is_prime, prime_generator


class TestPrimeGenerator(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(11))

    def test_prime_generator(self):
        self.assertEqual(prime_generator(0, 10), [2, 3, 5, 7])
        self.assertEqual(prime_generator(10, 20), [11, 13, 17, 19])
        self.assertEqual(prime_generator(20, 30), [23, 29])
        self.assertEqual(prime_generator(30, 40), [31, 37])
        self.assertEqual(prime_generator(40, 50), [41, 43, 47])
        self.assertEqual(prime_generator(50, 60), [53, 59])
        self.assertEqual(prime_generator(60, 70), [61, 67])
        self.assertEqual(prime_generator(70, 80), [71, 73, 79])
        self.assertEqual(prime_generator(80, 90), [83, 89])
        self.assertEqual(prime_generator(90, 102), [97, 101])


if __name__ == "__main__":
    unittest.main()
