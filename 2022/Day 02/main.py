import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        # first value in his hand (A, B, C) second value in line is my hand (X, Y, Z) - rock, paper, scissor in this order
        return [tuple(line.strip().split(" ")) for line in file]


# A Y
# B X
# C Z
rules = {
    # rock, rock
    ("A", "X"): 4,
    ("A", "Y"): 8,
    ("A", "Z"): 3,
    # paper, rock
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    # scissors, rock
    ("C", "X"): 7,
    ("C", "Y"): 2,
    ("C", "Z"): 6,

}

# how to change my hand according to his play if you "want" to win draw or lose
draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

# dict for part 2
rules_part_2 = {
    # rock, rock
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    # paper, rock
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    # scissors, rock
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7,

}


def total_score_according_rules(file_name):
    return sum(rules[game] for game in read_lines(file_name))


# change second value in tuple (my input) to mach lose (X), draw (Y), win (Z), change second value according to first one
# my hand is second "value" X, Y, Z
def score_according_to_my_hand(file_name):
    counter = 0
    for his_hand, my_hand in read_lines(file_name):
        # case need to lose
        if my_hand == "X":
            my_hand = lose[his_hand]
        # case need to draw
        elif my_hand == "Y":
            my_hand = draw[his_hand]
        # case need to win
        else:
            my_hand = win[his_hand]
        counter += rules[(his_hand, my_hand)]
    return counter


def score_according_to_my_hand(file_name):
    return sum(rules_part_2[game] for game in read_lines(file_name))


print("First part: ", total_score_according_rules(l))
print("Second part: ", score_according_to_my_hand(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(total_score_according_rules(self.s), 15)
        self.assertEqual(total_score_according_rules(self.l), 10941)

    def test_part_2(self):
        self.assertEqual(score_according_to_my_hand(self.s), 12)
        self.assertEqual(score_according_to_my_hand(self.l), 13071)