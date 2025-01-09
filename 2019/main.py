import unittest

s = "small_input.txt"
l = "input.txt"


def divide_and_subtract(number: int):
    return number // 3 - 2


def divide_until_0(number):
    counter = 0
    while number > 0:
        number = divide_and_subtract(number)
        if number >= 0:
            counter += number
    return counter


def sum_of_divide_and_subtract(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return sum(divide_and_subtract(int(line)) for line in file)


def sum_of_divide_until_0(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return sum(divide_until_0(int(line)) for line in file)


print("First part: ", sum_of_divide_and_subtract(l))
print("Second part: ", sum_of_divide_until_0(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_divide_until_0(self):
        self.assertEqual(divide_until_0(100756), 50346)
        self.assertEqual(divide_until_0(1969), 966)

    def test_part_1(self):
        self.assertEqual(sum_of_divide_and_subtract(self.s), 33583)
        self.assertEqual(sum_of_divide_and_subtract(self.l), 3553700)

    def test_part_2(self):
        self.assertEqual(sum_of_divide_until_0(self.l), 5327664)