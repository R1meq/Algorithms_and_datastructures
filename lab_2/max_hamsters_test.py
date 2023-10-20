import unittest

from lab_2.max_hamsters import max_hamsters


class MyTestCase(unittest.TestCase):
    def test_array1(self):
        array1 = [
            [2, 2],
            [1, 2],
            [3, 1],
        ]
        self.assertEqual(max_hamsters(7, 3, array1), 2)

    def test_array2(self):
        array2 = [
            [5, 0],
            [2, 2],
            [1, 4],
            [5, 1],
        ]
        self.assertEqual(max_hamsters(19, 4, array2), 3)

    def test_array3(self):
        array3 = [
            [1, 1000],
            [1, 6000],
        ]
        self.assertEqual(max_hamsters(2, 2, array3), 1)

    def test_array4(self):
        array4 = [
            [5, 1000],
            [10, 6000],
        ]
        self.assertEqual(max_hamsters(2, 2, array4), 0)

    def test_array5(self):
        def test_array1(self):
            array1 = [
                [1, 2],
                [2, 2],
                [3, 1],
                [4, 5],
                [5, 3],
                [6, 4],
                [7, 6],
                [8, 2],
                [9, 5],
                [10, 7],
                [11, 1],
                [12, 3],
                [13, 2],
                [14, 5],
                [15, 1],
            ]
            self.assertEqual(max_hamsters(20, 5, array1), 5)
