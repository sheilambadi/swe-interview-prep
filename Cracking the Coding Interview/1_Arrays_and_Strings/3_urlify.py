"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.) 

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"

Hints: 
#53: It's often easiest to modify strings by going from the end of the string to the beginning. 
#118: You might find you need to know the number of spaces. Can you just count them?
"""

import unittest

def urlify_replace(text, true_length):
    # modify same variable to ensure space is not wasted
    text = text[:true_length] # get length of string under consideration
    text = text.replace(' ', '%20') # use built-in function

    return text

def urlify(text, true_length):
    # Time complexity: 0(n) -> because of for-loop
    
    space = '%20'
    text = text[:true_length] # get length of string under consideration
    new_text = []

    for char in text:
        if char == ' ':
            new_text.append(space)
        else:
            new_text.append(char)

    new_text = ''.join(new_text) 
    return new_text


class Test(unittest.TestCase):
    """
        Ref: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p03_urlify.py
    """

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify_replace, urlify]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()
