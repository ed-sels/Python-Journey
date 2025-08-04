def solve_maze(maze, x=0, y=0):
    rows, cols = len(maze), len(maze[0])
    if x == rows - 1 and y == cols - 1 and maze[x][y] == 0:
        return True

    if x >= rows or y >= cols or maze[x][y] == 1:
        return False
    maze[x][y] = 1
    if solve_maze(maze, x, y + 1) or solve_maze(maze, x + 1, y):
        return True
    maze[x][y] = 0
    return False

maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]
print("Path exists" if solve_maze([row[:] for row in maze]) else "No path found")