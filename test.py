import unittest
from main import *


class WorkForSaraTest(unittest.TestCase):
    def test_is_even_number(self):
        self.assertEqual(True, is_even_number(2))
        self.assertEqual(False, is_even_number(3))
