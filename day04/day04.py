
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

def is_valid(password: int) -> bool:
    password_s = str(password)
    if len(password_s) != 6:
        return False

    password_i = [int(s) for s in password_s]
    compare = password_i[0]
    found_pair = False
    for _, val in enumerate(password_i[1:]):
        if val < compare:
            return False
        else:
            if val == compare:
                found_pair = True
            compare = val

    return found_pair


assert not is_valid(123)
assert is_valid(111111)
assert not is_valid(223450)
assert not is_valid(123789)

# Your puzzle input is still 240298-784956
valid_words = [is_valid(password) for password in range(240298, 784956+1)]
print(sum(valid_words))  # 1150 for Part 1


