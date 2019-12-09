# This file is inspired by watching Joel Grus live code

"""
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
"""
def fuel(mass: int) -> int:
    return max(mass // 3 - 2, 0)


assert fuel(12) == 2
assert fuel(14) == 2
assert fuel(1969) == 654
assert fuel(100756) == 33583

with open('input_fuel_counter.txt') as f:
    masses = [int(mass) for mass in f.read().splitlines()]
    fuel_part1 = sum(fuel(mass) for mass in masses)
print(fuel_part1)


# Part 2 - fuel for the mass and the fuel, recursively

def total_fuel(mass: int) -> int:
    needed_fuel = 0

    while mass > 0:
        next_fuel = fuel(mass)
        needed_fuel += next_fuel
        mass = next_fuel

    return needed_fuel


assert total_fuel(14) == 2
assert total_fuel(1969) == 966
assert total_fuel(100756) == 50346

fuel_part2 = sum(total_fuel(mass) for mass in masses)
print(fuel_part2)
