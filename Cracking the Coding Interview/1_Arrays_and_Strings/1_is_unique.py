"""
    Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
    cannot use additional data structures?
"""

import unittest
from collections import Counter


def is_unique_dict(word):
    # Time complexity: O(N) -> counter used
    counts = Counter(word)
    vals = list(counts.values())

    return all(v == 1 for v in vals)

def is_unique(word):
    """
        Implementation without an additional data structure
    """
    # Time complexity: O(N) -> for loop

    # store previous letter in sorted list
    sorted_word = sorted(word)
    previous_word = ''

    # check if letter equals previous letter, if so return that the list is not unique
    for l in sorted_word:
        if l == previous_word:
            return False
        else:
            previous_word = l

    return True

class Test(unittest.TestCase):
    """
        Adapted from: https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/1_Is%20Unique/IsUnique.py
    """
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_is_unique_dict(self):
        for test_string in self.dataT:
            actual = is_unique_dict(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique_dict(test_string)
            self.assertFalse(actual)

    def test_is_unique(self):
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()