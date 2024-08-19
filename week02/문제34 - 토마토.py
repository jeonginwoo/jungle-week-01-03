"""
출처 : 백준
번호 : 7569
난이도 : 골드 5
제목 : 토마토
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS():
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    day = 0
    count = [[[0] * M for _ in range(N)] for __ in range(H)]
    queue = deque()
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    queue.append([x, y, z])
                    count[z][y][x] = 1
                if box[z][y][x] == -1:
                    count[z][y][x] = -1
    while queue:
        now_x, now_y, now_z = queue.popleft()
        for go in range(6):
            next_x = now_x + dx[go]
            next_y = now_y + dy[go]
            next_z = now_z + dz[go]
            if (0 <= next_x < M
                    and 0 <= next_y < N
                    and 0 <= next_z < H
                    and not count[next_z][next_y][next_x]):
                count[next_z][next_y][next_x] = count[now_z][now_y][now_x] + 1
                queue.append([next_x, next_y, next_z])
        day = count[now_z][now_y][now_x] - 1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if count[z][y][x] == 0:
                    return -1
    return day


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]

print(BFS())

