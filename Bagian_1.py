import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_position = (current_node.position[0] + dx, current_node.position[1] + dy)

            if (0 <= new_position[0] < len(maze) and
                0 <= new_position[1] < len(maze[0]) and
                maze[new_position[0]][new_position[1]] == 0 and
                new_position not in closed_set):

                neighbor = Node(new_position, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor.position, goal_node.position)
                neighbor.f = neighbor.g + neighbor.h

                heapq.heappush(open_list, neighbor)
    return None

# Catatan: 0 = jalan, 1 = rintangan
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(maze, start, goal)

if path:
    print("Jalur ditemukan:")
    for step in path:
        print(step)
else:
    print("Tidak ada jalur ke tujuan.")
