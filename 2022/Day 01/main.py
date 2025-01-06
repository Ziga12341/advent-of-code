import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        elfs_calories = []
        elf_calories = []
        for line in file:
            if line == "\n":
                elfs_calories.append(elf_calories)
                elf_calories = []
            else:
                elf_calories.append(int(line))
        elfs_calories.append(elf_calories)
        return elfs_calories


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def sum_calories_and_get_max(file_name):
    return sorted(sum(elf_calories) for elf_calories in read_lines(file_name))[-1]  # take the last one


def sum_calories_from_top_3(file_name):
    return sum(sorted(sum(elf_calories) for elf_calories in read_lines(file_name))[-3:]) # take last 3 and sum them


print("First part: ", sum_calories_and_get_max(l))
print("Second part: ", sum_calories_from_top_3(l))


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.small_input: list[str] = read_lines(s)

    def test_part_1(self):
        self.assertEqual(sum_calories_and_get_max(s), 24000)
        self.assertEqual(sum_calories_and_get_max(l), 71471)

    def test_part_2(self):
        self.assertEqual(sum_calories_from_top_3(s), 45000)
        self.assertEqual(sum_calories_from_top_3(l), 211189)