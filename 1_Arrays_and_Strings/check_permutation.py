"""
    Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.
"""
import unittest

def check_permutation(string1, string2):
    # Time complexity O(n log n) - because sorted used
    # Space complexity O(n) - string copied
    
    if len(string1) != len(string2):
        return False
    else:
        sorted1 = sorted(string1)
        sorted2 = sorted(string2)

        if sorted1 == sorted2:
            return True
        else:
            return False


class Test(unittest.TestCase):
    """
        Ref: https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/2_Check%20Permutation/CheckPermutation.py
    """
    dataT = (
        ("abcd", "bacd"),
        ("3563476", "7334566"),
        ("wef34f", "wffe34"),
    )
    dataF = (
        ("abcd", "d2cba"),
        ("2354", "1234"),
        ("dcw4f", "dcw5f"),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
