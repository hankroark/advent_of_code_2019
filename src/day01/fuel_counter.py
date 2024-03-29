# This file is my own take at day 1.  As it stands, it only calculate part 2.

def read_data():
    path = "input_fuel_counter.txt"
    with open(path, 'r') as file:
        data = [int(s) for s in file.read().splitlines()]
    return data


def calculate_module_fuel(masses, include_fuel_for_fuel=False):
    module_only_fuel = [(module_mass // 3) - 2 for module_mass in masses]
    if include_fuel_for_fuel:
        extra_fuel = [calculate_fuel_for_fuel(mf) for mf in module_only_fuel]
    else:
        extra_fuel = [0 for mf in module_only_fuel]
    return [sum(x) for x in zip(module_only_fuel, extra_fuel)]

def calculate_total_fuel(module_fuel):
    return sum(module_fuel)

def calculate_fuel_for_fuel(fuel_mass):
    extra_fuel = 0
    while fuel_mass > 0:
        incremental_fuel = (fuel_mass // 3 - 2)
        extra_fuel += max(incremental_fuel, 0)
        fuel_mass = incremental_fuel
    return extra_fuel

def day01_get_results(modules_masses):
    module_fuel = calculate_total_fuel(calculate_module_fuel(modules_masses, False))
    total_fuel = calculate_total_fuel(calculate_module_fuel(modules_masses, True))
    return module_fuel, total_fuel


if __name__ == "__main__":
    # calculate_fuel_for_fuel(654)
    modules_masses = read_data()
    results = day01_get_results(modules_masses)
    print(results)
