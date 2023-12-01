import unittest

from lab_6.src.finite_automata_string_match import search_pattern_in_text


class FiniteAutomataTest(unittest.TestCase):
    def test_1(self):
        pattern = "AB"
        text = "AAAAB"

        self.assertEqual([3], search_pattern_in_text(pattern, text))

    def test_2(self):
        pattern = "AAAA"
        text = "AB"

        self.assertEqual([], search_pattern_in_text(pattern, text))

    def test_3(self):
        pattern = " "
        text = "AAAAAB"

        self.assertEqual([], search_pattern_in_text(pattern, text))

    def test_4(self):
        pattern = "ABAB"
        text = "ABABABABABAB"

        self.assertEqual([0, 2, 4, 6, 8], search_pattern_in_text(pattern, text))

