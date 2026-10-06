import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        all_dimensions = []
        for line in file:
            # lwh is dimensions (length l, width w, and height h)
            dimensions = tuple(int(lwh) for lwh in line.strip().split("x"))
            all_dimensions.append(dimensions)
        return all_dimensions


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def part_1(file_name):
    # lwh is dimensions (length l, width w, and height h)
    sum_all_gifts_surfaces_area = 0
    for l, w, h in read_lines(file_name):
        surface_area_of_one_gift = 2*l*w + 2*w*h + 2*h*l
        # add also additional paper - extra paper for each present: the area of the smallest side
        sorted_dimensions = sorted((l, w, h))
        extra_paper = sorted_dimensions[0] * sorted_dimensions[1]
        sum_all_gifts_surfaces_area += surface_area_of_one_gift + extra_paper
    return sum_all_gifts_surfaces_area



def part_2(file_name):
    # lwh is dimensions (length l, width w, and height h)
    sum_ribbon_length = 0
    for l, w, h in read_lines(file_name):
        ribbon_for_bow = l * w * h
        sorted_dimensions = sorted((l, w, h))
        smallest_dimensions = sorted_dimensions[0]
        second_smallest_dimensions = sorted_dimensions[1]
        ribbon_to_warp_present = smallest_dimensions * 2 + second_smallest_dimensions * 2
        sum_ribbon_length += ribbon_for_bow + ribbon_to_warp_present
    return sum_ribbon_length


        
        
print("First part small: ", part_1(s))
print("First part: ", part_1(l))
print("Second part: ", part_2(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_part_1(self):
        self.assertEqual(part_1(self.s), 58)
        self.assertEqual(part_1(self.l), 1586300)

    def test_part_2(self):
        self.assertEqual(part_2(self.s), 34)
        self.assertEqual(part_2(self.l), 3737498)
