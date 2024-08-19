"""
출처 : 백준
번호 : 2178
난이도 : 실버 1
제목 : 미로 탐색
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque()
    queue.append((0, 0))
    while queue:
        now = queue.popleft()
        for go in range(4):
            next_x = now[0] + dx[go]
            next_y = now[1] + dy[go]
            if 0 <= next_x < N and 0 <= next_y < M and miro[next_x][next_y] == 1 and (next_x, next_y) != (0, 0):
                queue.append((next_x, next_y))
                miro[next_x][next_y] = miro[now[0]][now[1]] + 1


N, M = map(int, input().split())
miro = [[int(x) for x in input().strip()] for _ in range(N)]
count = [[0] * M for _ in range(N)]
BFS()
print(miro[-1][-1])

