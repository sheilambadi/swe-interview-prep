"""
Convert numeric string to number without using Python's built in functions.

Ref: https://stackoverflow.com/a/46406388/8398363 
The trick is that 546 = 500 + 40 + 6, or 5*10^2 + 4*10^1 + 6*10^0.
Note how the exponent is just the index (in reverse). Using that, you can generalize this approach into a function.
"""

char_digit = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def string_to_int_reversed(num_str):
    number = 0
    for idx, num in enumerate(reversed(num_str)):
        number += char_digit[num] * (10 ** idx)

    print(number)
    assert isinstance(number, int)

def string_to_int(num_str):
    number = 0
    str_len = len(num_str) - 1

    for num in num_str:
        number += char_digit[num] * (10 ** str_len)
        str_len -= 1

    print(number)
    assert isinstance(number, int)

str_no = "546"
print(type(str_no))

string_to_int_reversed(str_no)
string_to_int(str_no)