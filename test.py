import unittest
from main import *


class WorkForSaraTest(unittest.TestCase):
    def test_is_even_number(self):
        self.assertEqual(True, is_even_number(2))
        self.assertEqual(False, is_even_number(3))

    def test_do_next_step(self):
        self.assertEqual(9, do_next_step(18))
        self.assertEqual(28, do_next_step(9))

    def test_count_steps(self):
        self.assertEqual(20, count_steps(18))

    def test_generate_range(self):
        expected_range = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }
        self.assertEquals(expected_range, generate_range(1, 5))

    def test_get_count_of_steps_for_every_number(self):
        expected_range = {
            1: 0,
            2: 1,
            3: 7,
            4: 2,
            5: 5
        }
        self.assertEquals(expected_range, get_count_of_steps_for_every_number(1, 5))

    def test_find_the_highest_count_of_steps(self):
        actual_range = {
            1: 0,
            2: 1,
            3: 7,
            4: 2,
            5: 5
        }
        self.assertEquals("7 3", find_the_highest_count_of_steps(actual_range, 1, 5))

    def test_read_line_from_file(self):
        self.assertEquals("2\n", read_line_from_file("test_input.txt", 1))

    def test_parse_range(self):
        self.assertEquals([10, 20], parse_range("10 20"))

    def test_generate_output_file(self):
        self.assertEquals("20 18\n111 27", generate_output_file("test_input.txt"))
