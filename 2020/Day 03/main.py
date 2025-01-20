import unittest

s = "small_input.txt"
l = "input.txt"

# for part two you should use this list of slopes
# first is right second is down
slopes = [
    (1, 1),
    (3, 1),  # this one is for part one
    (5, 1),
    (7, 1),
    (1, 2)]


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def count_trees_move_n_right_and_m_down(file_name, right=3, down=1):
    trees = 0
    # take grid lines by step (if step 2 take each second line)
    # do not start with the first line (start with the second)
    # initialize down steps in lines
    for i, line in enumerate(read_lines(file_name)[::down]):
        # modulus operator, % (modulo) operator also called the remainder
        # I use this because when end of line you need to add the whole grid on the right
        trees += line[i * right % len(line)] == "#"
    return trees


# solution in one line for part one
def count_trees_move_n_right_and_m_down(file_name, right=3, down=1):
    # take grid lines by step (if step 2 take each second line)
    # do not start with the first line (start with the second)
    # initialize down steps in lines
    # modulus operator, % (modulo) operator also called the remainder,
    # I use this because when end of line you need to add the whole grid on the right
    return sum(line[i * right % len(line)] == "#" for i, line in enumerate(read_lines(file_name)[::down]))


def multiply_counted_trees_different_slopes_for_the_same_grid(file_name):
    multiply_trees_each_slope = 1
    for right, down in slopes:
        multiply_trees_each_slope *= count_trees_move_n_right_and_m_down(file_name, right, down)
    return multiply_trees_each_slope


print("First part: ", count_trees_move_n_right_and_m_down(l))
print("Second part: ", multiply_counted_trees_different_slopes_for_the_same_grid(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(count_trees_move_n_right_and_m_down(self.s), 7)
        self.assertEqual(count_trees_move_n_right_and_m_down(self.l), 254)

    def test_part_2(self):
        self.assertEqual(multiply_counted_trees_different_slopes_for_the_same_grid(self.s), 336)
        self.assertEqual(multiply_counted_trees_different_slopes_for_the_same_grid(self.l), 1666768320)