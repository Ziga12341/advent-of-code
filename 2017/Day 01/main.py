import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return [int(char.strip()) for line in file for char in line]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)
print(large_input)


def check_sequence_sum_of_repeated_numbers(file_name):
    counter = 0
    sequence = read_lines(file_name)
    # check first and last
    if sequence[0] == sequence[-1]:
        counter += sequence[0]
    for number1, number2 in zip(sequence, sequence[1:]):
        if number1 == number2:
            counter += number1
    return counter


def part_2(file_name):
    ...


print("First part: ", check_sequence_sum_of_repeated_numbers(l))
print("Second part: ", part_2(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(check_sequence_sum_of_repeated_numbers(self.l), 1029)

    def test_part_2(self):
        self.assertEqual(part_2(self.s), None)