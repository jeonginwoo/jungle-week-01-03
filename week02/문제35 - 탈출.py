"""
출처 : 백준
번호 : 3055
난이도 : 골드 4
제목 : 탈출
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue_w = deque()
    queue_s = deque()

    for i in range(R):
        for j in range(C):
            if grid[i][j] == "*":
                queue_w.append((i, j))
            elif grid[i][j] == "S":
                grid[i][j] = 0
                queue_s.append((i, j))

    while queue_s:
        # 물 이동
        for _ in range(len(queue_w)):
            wx, wy = queue_w.popleft()
            for i in range(4):
                next_wx, next_wy = wx + dx[i], wy + dy[i]
                if 0 <= next_wx < R and 0 <= next_wy < C and grid[next_wx][next_wy] == ".":
                    grid[next_wx][next_wy] = "*"
                    queue_w.append((next_wx, next_wy))

        # 고슴도치 이동
        for _ in range(len(queue_s)):
            sx, sy = queue_s.popleft()
            for i in range(4):
                next_sx, next_sy = sx + dx[i], sy + dy[i]
                if 0 <= next_sx < R and 0 <= next_sy < C:
                    if grid[next_sx][next_sy] == "D":
                        return grid[sx][sy] + 1
                    if grid[next_sx][next_sy] == ".":
                        grid[next_sx][next_sy] = grid[sx][sy] + 1
                        queue_s.append((next_sx, next_sy))

    return "KAKTUS"


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

print(BFS())
