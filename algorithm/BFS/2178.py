import sys
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sys_input():
    return sys.stdin.readline().rstrip()

def bfs(n, m, board, start):
    dist = [[-1] * m for _ in range(n)]
    queue = deque([start])
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and board[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist

def solve(n, m, board):
    dist = bfs(n, m, board, (0, 0))
    return dist[n - 1][m - 1] + 1

def main():
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input())) for _ in range(n)]

    answer = solve(n, m, board)
    print(answer)

if __name__ == "__main__":
    main()