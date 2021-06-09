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
