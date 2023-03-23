import unittest

def more(a):
    b = str(a)
    return(b*2)

def is_nine(a):
    if a == 9:
        return True
    else:
        return False

def add_1(a):
    return a+1

def reverse(a):
    return a[::-1]

class TestStringMethods(unittest.TestCase):

    def test_more(self):
        self.assertIn('33', more('3'))
        self.assertNotIn('2', more('3'))

    def test_reverse(self):
        self.assertEqual('fd', reverse('fd'))

if __name__ == '__main__':
    unittest.main()

class NumbersTest(unittest.TestCase):

    def test_is_nine(self):
        self.assertTrue(is_nine(9))
        self.assertFalse(is_nine(4))

    def test_add_1(self):
        self.assertGreater(add_1(1), 1)
        self.assertLess(1, add_1(1))


if __name__ == '__main__':
    unittest.main()

