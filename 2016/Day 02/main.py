import unittest
from collections import Counter

s = "small_input.txt"
l = "input.txt"

direction_change = {"U": (0, -1),
                    "D": (0, 1),
                    "R": (1, 0),
                    "L": (-1, 0)
                    }

# the idea is to change position only if we can

# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]

position = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
# it should go y and then x

# this is for mapping back from buttons to position of button
buttons_to_positions = {1: (0, 0),
                        2: (1, 0),
                        3: (2, 0),
                        4: (0, 1),
                        5: (1, 1),
                        6: (2, 1),
                        7: (0, 2),
                        8: (1, 2),
                        9: (2, 2)
                        }


# we go buy index
# [0, 1, 2]
# [0, 1, 2]
# [0, 1, 2]

def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


# need to use y first and than x in position[y][x]
# if there is possible to change position change it... return a value
def next_step(direction: str, previous_button_pressed: int = 5):
    x0, y0 = buttons_to_positions[previous_button_pressed]
    x1, y1 = direction_change[direction]
    x_new = x0 + x1
    y_new = y0 + y1
    if 0 <= x_new <= 2 and 0 <= y_new <= 2:
        return position[y_new][x_new]
    return position[y0][x0]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)
print(small_input)


def part_1(file_name: str) -> int:
    final_number = ""
    # starting number; each iteration start where you stayed
    current_button = 5
    for line in read_lines(file_name):
        for direction in line:
            current_button = next_step(direction, current_button)
        final_number += str(current_button)
    return int(final_number)


def part_2(file_name):
    ...


print("First part: ", part_1(l))
print("Second part: ", part_2(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_next_step(self):
        self.assertEqual(next_step("R", 6), 6)
        self.assertEqual(next_step("U"), 2)
        self.assertEqual(next_step("L", 9), 8)

    def test_part_1(self):
        self.assertEqual(part_1(self.s), 1985)
        self.assertEqual(part_1(self.l), 18843)

    def test_part_2(self):
        self.assertEqual(part_2(self.s), None)
