import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        # i had bug with number forward bigger then 9
        return [(element[0], int(element[1:])) for element in file.readline().strip().split(", ")]


# 0 - north
# 1 - east
# 2 - south
# 3 - west

def blocks_away_from_start(file_name):
    sequence = read_lines(file_name)
    starting_direction = 0  # start's facing north
    x = 0
    y = 0
    for direction, forward in sequence:
        # case for turning right
        if direction == "R":
            if starting_direction == 3:
                y += forward
            elif starting_direction == 2:
                x -= forward
            elif starting_direction == 1:
                y -= forward
            else:
                x += forward
            # if location 3 (west) need to go to north
            if starting_direction == 3:
                starting_direction = 0
            else:
                starting_direction += 1

        # case for turning left
        elif direction == "L":
            if starting_direction == 0:
                x -= forward
            elif starting_direction == 1:
                y += forward
            elif starting_direction == 2:
                x += forward
            else:
                y -= forward

            # if location north goes to west
            if starting_direction == 0:
                starting_direction = 3
            else:
                starting_direction -= 1

    return abs(x) + abs(y)


# Manhattan geometry from 0, 0 to location first visited twice
def first_location_visited_twice(file_name):
    sequence = read_lines(file_name)
    starting_direction = 0  # start's facing north
    x = 0
    y = 0
    visited = []
    for direction, forward in sequence:
        # case for turning right
        if direction == "R":
            # loop over forward to get x, y for each step and append it to vizited (check if you already on this location)
            for step in range(forward):

                if starting_direction == 3:
                    y += 1
                elif starting_direction == 2:
                    x -= 1
                elif starting_direction == 1:
                    y -= 1
                else:
                    x += 1

                if (x, y) in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append((x, y))
            # if location 3 (west) need to go to north
            if starting_direction == 3:
                starting_direction = 0
            else:
                starting_direction += 1

        # case for turning left
        elif direction == "L":
            # loop over forward to get x, y for each step and append it to vizited (check if you already on this location)

            for step in range(forward):
                if starting_direction == 0:
                    x -= 1
                elif starting_direction == 1:
                    y += 1
                elif starting_direction == 2:
                    x += 1
                else:
                    y -= 1

                if (x, y) in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append((x, y))
            # if location north goes to west
            if starting_direction == 0:
                starting_direction = 3
            else:
                starting_direction -= 1


print("First part: ", blocks_away_from_start(l))
print("Second part: ", first_location_visited_twice(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(blocks_away_from_start(self.s), 12)
        self.assertEqual(blocks_away_from_start("small_input2.txt"), 2)
        self.assertEqual(blocks_away_from_start("small_input3.txt"), 5)
        self.assertEqual(blocks_away_from_start("small_input4.txt"), 10)
        self.assertEqual(blocks_away_from_start(self.l), 209)

    def test_part_2(self):
        self.assertEqual(first_location_visited_twice("small_input5.txt"), 4)
        self.assertEqual(first_location_visited_twice(self.l), 136)