# Optimized 8-Puzzle using DFS

start = (
    5, 6, 4,
    0, 3, 1,
    7, 2, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = (
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    )

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c

            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos],
                new_state[zero]
            )

            yield tuple(new_state)


def dfs(start, goal, limit=200000):
    stack = [(start, 0)]
    visited = {start}
    parent = {start: None}

    while stack:
        state, depth = stack.pop()

        if state == goal:
            return build_path(parent, goal)

        if depth >= limit:
            continue

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = state
                stack.append((neighbor, depth + 1))

    return None


def build_path(parent, goal):
    path = []

    while goal is not None:
        path.append(goal)
        goal = parent[goal]

    return path[::-1]


def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step}")

        for i in range(0, 9, 3):
            print(state[i:i + 3])

        print()


# Solve
path = dfs(start, goal)

if path:
    print("DFS Solution Found")
    print("Steps:", len(path) - 1)
    print()
    print_path(path)
else:
    print("Solution not found within limit")
