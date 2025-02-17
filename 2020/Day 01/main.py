import unittest
import numpy as np

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return {int(line.strip()) for line in file}


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def find_values_that_sum_is_2020(file_name):
    whole_list_of_expenses = read_lines(file_name)
    for first in whole_list_of_expenses:
        for second in whole_list_of_expenses:
            if first + second == 2020:
                return first * second

# optimized solution
def find_values_that_sum_is_2020(file_name):
    whole_list_of_expenses = read_lines(file_name)
    for first in whole_list_of_expenses:
        if 2020 - first in whole_list_of_expenses:
            return first * (2020 - first)

# optimized solution with generator
def find_values_that_sum_is_2020(file_name):
    whole_list_of_expenses = read_lines(file_name)
    return next(first * (2020 - first) for first in whole_list_of_expenses if 2020 - first in whole_list_of_expenses)

def find_three_values_that_sum_2020(file_name):
    whole_list_of_expenses = read_lines(file_name)
    for first in whole_list_of_expenses:
        for second in whole_list_of_expenses:
            for third in whole_list_of_expenses:
                if first + second + third == 2020:
                    return first * second * third

# optimized solution
def find_three_values_that_sum_2020(file_name):
    whole_list_of_expenses = read_lines(file_name)
    for first in whole_list_of_expenses:
        for second in whole_list_of_expenses:
            if 2020 - first - second in whole_list_of_expenses:
                return first * second * (2020 - first - second)
# with generatto
def find_three_values_that_sum_2020(file_name):
    whole_list_of_expenses = read_lines(file_name)
    return next(first * second * (2020 - first - second) for second in whole_list_of_expenses for first in whole_list_of_expenses if 2020 - first - second in whole_list_of_expenses)

print("First part: ", find_values_that_sum_is_2020(l))
print("Second part: ", find_three_values_that_sum_2020(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(find_values_that_sum_is_2020(self.s), 514579)
        self.assertEqual(find_values_that_sum_is_2020(self.l), 970816)

    def test_part_2(self):
        self.assertEqual(find_three_values_that_sum_2020(self.s), 241861950)
        self.assertEqual(find_three_values_that_sum_2020(self.l), 96047280)