import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return [(line.strip()[:(len(line.strip()) // 2)], line.strip()[(len(line.strip()) // 2):]) for line in file]


def read_lines_part_two(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        all_rucksack_by_three = []
        accumulator = []
        for line in file:
            if len(accumulator) == 3:
                all_rucksack_by_three.append(tuple(accumulator))
                accumulator = []
                accumulator.append(line.strip())
            else:
                accumulator.append(line.strip())

        all_rucksack_by_three.append(tuple(accumulator))
        return all_rucksack_by_three


# ord("A") = 65
# ord("a") = 97
# a = 1
# A = 27
# lowercase ord(char) - 96
# uppercase ord(char) - 38
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def evaluate_prioritise_rearrangements(file_name):
    counter = 0
    for first_compartment, second_compartment in read_lines(file_name):
        # get union which char represented in both compartments
        item_type = set(first_compartment).intersection(set(second_compartment))
        item_type = item_type.pop()
        # if is lower letter
        if item_type.islower():
            counter += ord(item_type) - 96
        else:
            counter += ord(item_type) - 38
    return counter


def same_char_in_three_rucksack_sum(file_name):
    counter = 0
    for first_rucksack, second_rucksack, third_rucksack in read_lines_part_two(file_name):
        # get chat that is represented in all of three rucksacks
        item_type = set(first_rucksack) & set(second_rucksack) & set(third_rucksack)
        item_type = item_type.pop()
        # if is lower letter
        if item_type.islower():
            counter += ord(item_type) - 96
        else:
            counter += ord(item_type) - 38

    return counter


print("First part: ", evaluate_prioritise_rearrangements(l))
print("Second part: ", same_char_in_three_rucksack_sum(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(evaluate_prioritise_rearrangements(self.s), 157)
        self.assertEqual(evaluate_prioritise_rearrangements(self.l), 7908)

    def test_part_2(self):
        self.assertEqual(same_char_in_three_rucksack_sum(self.s), 70)
        self.assertEqual(same_char_in_three_rucksack_sum(self.l), 2838)