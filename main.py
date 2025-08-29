import sys
from bfs import bfs_solve

def read_maze(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        width, height = map(int, f.readline().split())
        maze = []
        for _ in range(height):
            line = f.readline().strip()
            maze.append(list(line))
        return maze

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <maze_file>")
        sys.exit(1)

    maze = read_maze(sys.argv[1])
    result = bfs_solve(maze)
    print(result)
