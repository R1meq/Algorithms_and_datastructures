from collections import deque

KNIGHT_X_COORDINATES = [2, 2, -2, -2, 1, 1, -1, -1]
KNIGHT_Y_COORDINATES = [-1, 1, 1, -1, 2, -2, 2, -2]
LENGTH = len(KNIGHT_X_COORDINATES)


class Vertex:
    def __init__(self, x, y, step=0):
        self.x = x
        self.y = y
        self.step = step

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def is_within_board(x, y, board_size):
    return 0 <= x < board_size and 0 <= y < board_size


def find_shortest_distance(src, dest, board_size):
    visited = set()
    queue = deque()

    queue.append(src)
    visited.add(src)
    while queue:
        node = queue.popleft()
        x, y, step = node.x, node.y, node.step
        print(f"[x: {x}, y: {y}] step: {step}")

        if x == dest.x and y == dest.y:
            with open("../test/output.txt", "w") as output_file:
                output_file.write(str(step))
            return step

        for k in range(LENGTH):
            next_x = x + KNIGHT_X_COORDINATES[k]
            next_y = y + KNIGHT_Y_COORDINATES[k]
            next_step = step + 1

            if is_within_board(next_x, next_y, board_size):
                neighbor = Vertex(next_x, next_y, next_step)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    return -1
