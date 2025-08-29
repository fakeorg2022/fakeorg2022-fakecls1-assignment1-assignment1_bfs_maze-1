from collections import deque

def bfs_solve(maze):
    """
    使用 BFS 求解迷宫最短路径
    输入: maze (二维列表), 其中:
        'S' 起点
        'E' 终点
        '0' 可通行
        '1' 墙壁
    输出: 最短路径步数 (int)，若无解返回 -1
    """
    if not maze or not maze[0]:
        return -1

    height = len(maze)
    width = len(maze[0])

    # 找起点和终点
    start, end = None, None
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 'S':
                start = (x, y)
            elif maze[y][x] == 'E':
                end = (x, y)

    if not start or not end:
        return -1

    # BFS 初始化
    queue = deque()
    visited = [[False] * width for _ in range(height)]

    queue.append((start[0], start[1], 0))  # (x, y, dist)
    visited[start[1]][start[0]] = True

    # 四个方向
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        x, y, dist = queue.popleft()

        # 到达终点
        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not visited[ny][nx] and maze[ny][nx] in ('0','E'):
                    visited[ny][nx] = True
                    queue.append((nx, ny, dist + 1))

    return -1
