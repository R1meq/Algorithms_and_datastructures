import unittest

from lab_1.traverse_zigzag import traverse_zigzag


class TestTraverseZigzag(unittest.TestCase):

    def setUp(self):
        self.input_1 = [
            [1, 2, 6, 7, 15],
            [3, 5, 8, 14, 16],
            [4, 9, 13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25]
        ]
        self.input_2 = [
            [1, 2, 5, 6],
            [3, 4, 7, 8]
        ]
        self.input_3 = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        self.input_4 = [
            [1]
        ]
        self.output_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self.output_2 = [1,2,3,4,5,6,7,8]
        self.output_3 = [1,2,3,4,5,6]
        self.output_4 = [1]

    def test_traverse_zigzag_1(self):
        self.assertEqual(traverse_zigzag(self.input_1), self.output_1)

    def test_traverse_zigzag_2(self):
        self.assertEqual(traverse_zigzag(self.input_2), self.output_2)

    def test_traverse_zigzag_3(self):
        self.assertEqual(traverse_zigzag(self.input_3), self.output_3)

    def test_traverse_zigzag_4(self):
        self.assertEqual(traverse_zigzag(self.input_4), self.output_4)

