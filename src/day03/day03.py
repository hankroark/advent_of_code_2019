from typing import List, Tuple

Move = Tuple[str, int]
Path = List[Move]
Point = Tuple[int, int]
Locations = List[Point]

"""
Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""
def closest_crossing(wire_1 : Path, wire_2 : Path, origin_distance=True) -> int:
    locations_1 = get_locations(wire_1)
    locations_2 = get_locations(wire_2)
    crossings = calc_crossings(locations_1, locations_2)
    if origin_distance:
        distances = manhattan_distances(crossings)
    else:
        distances = wire_length_distances(locations_1, locations_2, crossings)

    return min(distances)

def calc_crossings(wire_1_locs : Locations, wire_2_locs : Locations) -> Locations:
    return list(set(wire_1_locs) & set(wire_2_locs))

def get_locations(wire: Path) -> Locations:
    x = y = 0
    locations_visited = list()
    for segment in wire:
        travel_direction, travel_distance = segment[0], segment[1]
        for _ in range(travel_distance):
            if travel_direction == 'R':
                x += 1
            elif travel_direction == 'L':
                x -= 1
            elif travel_direction == 'U':
                y += 1
            elif travel_direction == 'D':
                y -= 1
            else:
                raise RuntimeError(f"Bad direction : {travel_direction}")

            current_location = (x, y)
            locations_visited.append(current_location)

    return locations_visited

def manhattan_distances(points: Locations) -> List[int]:
    return [abs(location[0])+abs(location[1]) for location in points]

def wire_length_distances(wire_1: Locations, wire_2: Locations, crossings: Locations) -> List[int]:
    return [wire_1.index(crossing) + wire_2.index(crossing) + 2 for crossing in crossings]

def parse_path(path: str) -> Path:
    steps = path.split(',')
    return [(step[0], int(step[1:])) for step in steps]

def day03_get_results(wire1path: str, wire2path: str) -> Tuple[str, str]:
    wire_1, wire_2 = parse_path(wire1path), parse_path(wire2path)
    return closest_crossing(wire_1, wire_2), closest_crossing(wire_1, wire_2, False)


if __name__ == "__main__":
    # Tests
    short_wire = [('R',8),('U',5),('L',5),('D',3)]
    locations_short = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),
                   (7,5),(6,5),(5,5),(4,5),(3,5),(3,4),(3,3),(3,2)]
    assert get_locations(short_wire) == locations_short

    wire_1 = [('R',75),('D',30),('R',83),('U',83),('L',12),('D',49),('R',71),('U',7),('L',72)]
    wire_2 = [('U',62),('R',66),('U',55),('R',34),('D',71),('R',55),('D',58),('R',83)]
    assert closest_crossing(wire_1, wire_2) == 159

    path_1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    path_2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    assert parse_path(path_1) == [('R',98),('U',47),('R',26),('D',63),('R',33),('U',87),('L',62),('D',20),('R',33),('U',53),('R',51)]
    wire_1, wire_2 = parse_path(path_1), parse_path(path_2)
    assert closest_crossing(wire_1, wire_2) == 135

    # Actual problem, Part 1
    with open('input.txt') as f:
        wires = f.readlines()

    print(day03_get_results(wires[0], wires[1]))


