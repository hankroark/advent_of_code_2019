from collections import Counter
from typing import List

"""
111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
"""

def is_valid(password: int, exact_pair=False) -> bool:
    password_s = str(password)
    if len(password_s) != 6:
        return False

    password_i = [int(s) for s in password_s]
    compare = password_i[0]
    for _, val in enumerate(password_i[1:]):
        if val < compare:
            return False
        compare = val

    counts = Counter(password_s)
    if not exact_pair:
        found_pair = max(counts.values()) > 1
    else:
        found_pair = 2 in counts.values()

    return found_pair


assert not is_valid(123)
assert is_valid(111111)   # ok for part 1
assert not is_valid(223450)
assert not is_valid(123789)


"""
Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""
assert not is_valid(111111, exact_pair=True) # part 2 rules
assert is_valid(112233, exact_pair=True)
assert not is_valid(123444, exact_pair=True)
assert is_valid(111122, exact_pair=True)

def day04_get_results(start_password: int, end_password: int) -> List[int]:
    valid_words_part_1 = sum([is_valid(password, False) for password in range(start_password, end_password + 1)])
    valid_words_part_2 = sum([is_valid(password, True ) for password in range(start_password, end_password + 1)])
    return [valid_words_part_1, valid_words_part_2]


# Your puzzle input is still 240298-784956
if __name__ == "__main__":
    print(day04_get_results(240298, 784956))

