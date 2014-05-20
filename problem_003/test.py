import unittest

def isPalindrome(a):
    n = str(a)

    """
    We're checking if the string representation of n equals the inverted string representation of n
    The [::-1] slice takes care of inverting the string
    After that, we compare for equality using ==
    """
    #[::-1] is advanced slicing. [a:b:c] means slice from a (inclusive) to b (exclusive) with step size c
    return str(n) == str(n)[::-1]

class TestCase(unittest.TestCase):

    def test_isPal(self):
        # Is integar a Palindrome?
        self.assertTrue(isPalindrome(9009))
        self.assertTrue(isPalindrome(90009))

if __name__ == '__main__':
    unittest.main()


