"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
Hints: 
#106: You do not have to-and should not-generate all permutations. This would be very inefficient.
#121: What characteristics would a string that is a permutation of a palindrome have?
#134: Have you tried a hash table? You should be able to get this down to 0( N) time. 
#136: Can you reduce the space usage by using a bit vector?
"""

import unittest

from collections import Counter

def is_palindrome_permutation_pythonic(text):
    # convert to lowercase and store only alphanumeric chars
    text = ''.join(filter(str.isalpha, text.lower()))

    # get count of chars
    count = Counter(text)

    # get odd counts
    odd = [v for v in count.values() if v % 2 != 0 ]

    # check count of odd numbers and return
    return len(odd) <= 1

def is_palindrome_permutation(text):
    # convert to lowercase and store only alphanumeric chars
    text = ''.join(filter(str.isalpha, text.lower()))

    # count chars
    start_char = ord('a')
    end_char = ord('z')
    total_chars = (end_char - start_char) + 1 # zero-indexed

    char_count = [0] * total_chars

    # count number of characters in text
    for char in text:
        unicode = char_to_unicode(char)
        char_count[unicode] += 1

    # get odd counts
    odd = [v for v in char_count if v % 2 != 0 ]

    # check count of odd numbers and return
    return len(odd) <= 1


def char_to_unicode(char):
    char = ord(char) - ord('a')
    return char


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient, a nurse to nurse a patient so.", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [is_palindrome_permutation_pythonic, is_palindrome_permutation]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()