import unittest
from collections import Counter

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        passwords_with_policy = []
        for line in file:
            rules = line.strip().split(": ")[0]
            password = line.strip().split(": ")[1]
            letter = rules.split(" ")[1]
            numbers = rules.split(" ")[0]
            lowest_number = int(numbers.strip().split("-")[0])
            highest_number = int(numbers.strip().split("-")[1])
            # parse in tuple numbers are ints
            passwords_with_policy.append((lowest_number, highest_number, letter, password))

        return passwords_with_policy


# counter count letters and how many of them is in password
def valid_passwords_count_letters_policies(file_name):
    counter = 0
    database_list = read_lines(file_name)
    for lowest_number, highest_number, letter, password in database_list:
        count_letters = Counter(password)
        counter += lowest_number <= count_letters[letter] <= highest_number
    return counter


# shorter version in one line
def valid_passwords_count_letters_policies(file_name):
    return sum(
        lowest_number <= Counter(password)[letter] <= highest_number for lowest_number, highest_number, letter, password
        in read_lines(file_name))


# exactly one index of two numbers must match index in password (the right letter in password on the right index once)
# start index with 1
def valid_passwords_on_exactly_one_position(file_name):
    counter = 0
    database_list = read_lines(file_name)
    for lowest_number, highest_number, letter, password in database_list:
        counter += letter == password[lowest_number - 1] and letter != password[highest_number - 1] or letter != \
                   password[lowest_number - 1] and letter == password[highest_number - 1]
    return counter


# in one line
def valid_passwords_on_exactly_one_position(file_name):
    return sum(letter == password[lowest_number - 1] and letter != password[highest_number - 1] or letter != password[
        lowest_number - 1] and letter == password[highest_number - 1] for
               lowest_number, highest_number, letter, password in read_lines(file_name))


print("First part: ", valid_passwords_count_letters_policies(l))
print("Second part: ", valid_passwords_on_exactly_one_position(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(valid_passwords_count_letters_policies(self.s), 2)
        self.assertEqual(valid_passwords_count_letters_policies(self.l), 456)

    def test_part_2(self):
        self.assertEqual(valid_passwords_on_exactly_one_position(self.s), 1)
        self.assertEqual(valid_passwords_on_exactly_one_position(self.l), 308)