from collections import deque


row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
LENGTH = len(row)


class Node:
    def __init__(self, x, y, step=0):
        self.x = x
        self.y = y
        self.step = step

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


def find_shortest_distance(src, dest, N):
    visited = set()
    queue = deque()

    queue.append(src)
    visited.add(src)
    while queue:
        node = queue.popleft()
        x, y, step = node.x, node.y, node.step
        print(f"[x: {x}, y: {y}] step: {step}")

        if x == dest.x and y == dest.y:
            with open("output.txt", "w") as output_file:
                output_file.write(str(step))
            return step

        for k in range(LENGTH):
            x1 = x + row[k]
            y1 = y + col[k]
            step1 = step + 1

            if is_valid(x1, y1, N):
                neighbor = Node(x1, y1, step1)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    return -1
