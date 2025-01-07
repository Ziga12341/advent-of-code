import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def count_depth_increasing(file_name):
    counter = 0
    depth_measurement = read_lines(file_name)
    for first, second in zip(depth_measurement, depth_measurement[1:]):
        counter += second > first
    return counter


def include_calculation_for_tree_measurement(file_name):
    counter = 0
    depth_measurement = read_lines(file_name)
    for i in range(len(depth_measurement) - 2):
        # remove second 3 form first 3 increment by 1 (need to remove the last two)
        if sum(depth_measurement[1 + i: 4 + i]) - sum(depth_measurement[0 + i: 3 + i]) > 0:
            counter += 1
    return counter


print("First part: ", count_depth_increasing(l))
print("Second part: ", include_calculation_for_tree_measurement(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(count_depth_increasing(self.s), 7)
        self.assertEqual(count_depth_increasing(self.l), 1581)

    def test_part_2(self):
        self.assertEqual(include_calculation_for_tree_measurement(self.s), 5)