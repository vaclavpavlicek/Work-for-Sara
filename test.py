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
        range = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }
        self.assertEquals(range, generate_range(1, 5))

