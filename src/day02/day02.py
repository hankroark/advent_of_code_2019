from typing import List

Program = List[int]

"""
Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""
def run_int_code(program : Program) -> Program :
    idx = 0
    stop = False

    while idx < len(program) and not stop:
        op = program[idx]
        if op == 99:
            stop = True
        else:
            lh = program[ program[idx + 1] ]
            rh = program[ program[idx + 2] ]
            target = program[idx + 3]
            if op == 1:
                program[target] = lh + rh
            elif op == 2:
                program[target] = lh * rh
        idx = idx + 4
    return program


assert run_int_code([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert run_int_code([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert run_int_code([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert run_int_code([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
assert run_int_code([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

# Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to
# the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the
# program, replace position 1 with the value 12 and replace position 2 with the value 2.
# What value is left at position 0 after the program halts?
def alarm(program: Program, noun : int = 12, verb : int = 2) -> int:
    program_copy = program[:]
    program_copy[1] = noun
    program_copy[2] = verb
    run_int_code(program_copy)
    return program_copy[0]

def parse_program(program_string):
    return [int(c) for c in program_string.split(',')]

def input_for_target(program, target):
    for noun in range(0, 100):
        for verb in range(0, 100):
            alarm_result = alarm(program, noun, verb)
            if alarm_result == target:
                return 100*noun+verb

def day02_get_results(program_string, target):
    program = parse_program(program_string)
    part1 = alarm(program)
    part2 = input_for_target(program, target)
    return part1, part2


if __name__ == "__main__":
    with open('input.txt') as f:
        program_string = f.read()

    # Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb?
    # (For example, if noun=12 and verb=2, the answer would be 1202.)
    TARGET = 19690720
    print(day02_get_results(program_string, TARGET))
