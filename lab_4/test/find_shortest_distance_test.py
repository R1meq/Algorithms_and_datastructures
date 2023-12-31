import unittest

from lab_4.src.find_shortest_distance import find_shortest_distance, Vertex


class MyTestCase(unittest.TestCase):
    def test_shortest_distance(self):
        with open("input.txt", "r") as file:
            lines = file.readlines()
        src_x, src_y = map(int, lines[1].strip().split(", "))
        dest_x, dest_y = map(int, lines[2].strip().split(", "))

        N = int(lines[0].strip())
        src = Vertex(src_x, src_y)
        dest = Vertex(dest_x, dest_y)
        result = find_shortest_distance(src, dest, N)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
