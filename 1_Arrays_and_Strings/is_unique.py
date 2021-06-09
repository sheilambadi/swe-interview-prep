"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

from collections import Counter


def is_unique_dict(word):
    counts = Counter(word)
    vals = list(counts.values())

    return all(v == 1 for v in vals)

print(is_unique_dict("Hello"))
print(is_unique_dict("Helo"))

def is_unique(word):
    """
    Implementation without an additional data structure
    """

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

print(is_unique("Hello"))
print(is_unique("Helo"))