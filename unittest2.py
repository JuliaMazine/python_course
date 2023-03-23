import unittest
import random
randomlist = []
for i in range(0,5):
    n = random.random()
    randomlist.append(n)

class NumbersTest(unittest.TestCase):
    def test_0_n_1(self):
        for n in randomlist:
            with self.subTest("delete this message later", i=i):
                self.assertGreaterEqual(n, 1/2)

if __name__ == '__main__':
    unittest.main()