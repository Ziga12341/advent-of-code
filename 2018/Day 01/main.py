import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        list_of_frequencies = []
        for line in file:
            if line.startswith("+"):
                list_of_frequencies.append(int(line[1:]))
            elif line.startswith("-"):
                list_of_frequencies.append(-int(line[1:]))


        return list_of_frequencies


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)
print(large_input)


def sum_frequencies(file_name):
    return sum(read_lines(file_name))


def frequency_reached_twice(file_name):
    vizited = set()
    counter = 0
    twice = False
    frequencies = read_lines(file_name)
    while not twice:
        frequency = frequencies.pop(0)
        counter += frequency
        if counter not in vizited:
            vizited.add(counter)
        else:
            return counter
        frequencies.append(frequency)


print("First part: ", sum_frequencies(l))
print("Second part: ", frequency_reached_twice(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(sum_frequencies(self.l), 525)

    def test_part_2(self):
        self.assertEqual(frequency_reached_twice(self.s), None)