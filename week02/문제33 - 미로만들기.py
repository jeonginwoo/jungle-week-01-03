"""
출처 : 백준
번호 : 2665
난이도 : 골드 4
제목 : 미로만들기
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * N for _ in range(N)]
    temp = []
    count = 0
    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        now = queue.popleft()
        for go in range(4):
            next_x = now[0] + dx[go]
            next_y = now[1] + dy[go]
            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y]:
                    if next_x == next_y == N-1:
                        return count
                    visited[next_x][next_y] = True
                    if miro[next_x][next_y] == 0:
                        temp.append([next_x, next_y])
                        continue
                    queue.append([next_x, next_y])
        if not queue:
            queue = deque(temp)
            temp = []
            count += 1
    return count


N = int(input())
miro = [[int(x) for x in input().strip()] for _ in range(N)]
print(BFS())