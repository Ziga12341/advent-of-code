import unittest

s = "small_input.txt"
l = "input.txt"


def which_floor_at_the_end(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        floors = file.readline()
        # if ( we go one floor up else down
        return floors.count("(") - floors.count(")")


def position_when_enter_basement(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        current_floor = 0
        # on which index we enter floor - 1 (basement)
        for i, floor in enumerate(file.readline()):
            if current_floor == -1:
                return i
            else:
                if floor == "(":
                    current_floor += 1
                else:
                    current_floor -= 1


print("First part: ", which_floor_at_the_end(l))
print("Second part: ", position_when_enter_basement(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(which_floor_at_the_end(self.l), 138)

    def test_part_2(self):
        self.assertEqual(position_when_enter_basement(self.l), 1771)