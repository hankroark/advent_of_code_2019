from collections import Counter

"""
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password
on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

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

# Your puzzle input is still 240298-784956
valid_words = [is_valid(password) for password in range(240298, 784956+1)]
print(sum(valid_words))  # 1150 for Part 1


"""
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of 
matching digits.

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

valid_words = [is_valid(password, exact_pair=True) for password in range(240298, 784956+1)]
print(sum(valid_words))  # 748 for Part 2
