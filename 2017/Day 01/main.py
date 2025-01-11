import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        # put each element as int into a list
        return [int(char.strip()) for line in file for char in line]


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


# next digit, it wants you to consider the digit halfway around
# if the same digit half of sequence index forward
def check_element_with_element_half_sequence_ahead(file_name):
    counter = 0
    sequence = read_lines(file_name)
    # duplicate sequence for bigger int-s, case for second part of sequence
    two_sequences = sequence * 2
    index_half_way = len(sequence) // 2
    for i, element in enumerate(sequence):
        if element == two_sequences[i + index_half_way]:
            counter += element
    return counter


# better solution with modulo
def check_element_with_element_half_sequence_ahead(file_name):
    counter = 0
    sequence = read_lines(file_name)
    index_half_way = len(sequence) // 2
    for i, element in enumerate(sequence):
        # use modulo to wrap around the index
        if element == sequence[(i + index_half_way) % len(sequence)]:
            counter += element
    return counter


# solution in one line
def check_element_with_element_half_sequence_ahead(file_name):
    sequence = read_lines(file_name)
    return sum(
        element for i, element in enumerate(sequence)
        # if element the same as half of the sequence ahead
        if element == sequence[(i + len(sequence) // 2) % len(sequence)])


print("First part: ", check_sequence_sum_of_repeated_numbers(l))
print("Second part: ", check_element_with_element_half_sequence_ahead(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(check_sequence_sum_of_repeated_numbers(self.l), 1029)

    def test_part_2(self):
        self.assertEqual(check_element_with_element_half_sequence_ahead(self.s), 12)
        self.assertEqual(check_element_with_element_half_sequence_ahead(self.l), 1220)