import unittest

from lab_4.find_shortest_distance import find_shortest_distance, Node


class MyTestCase(unittest.TestCase):
    def test_shortest_distance(self):
        N = 8
        src = Node(7, 0, 0)
        dest = Node(0, 7, 0)
        result = find_shortest_distance(src, dest, N)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
