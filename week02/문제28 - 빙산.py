"""
출처 : 백준
번호 : 2573
난이도 : 골드 4
제목 : 빙산
"""

import sys

input = sys.stdin.readline


def DFS():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    year = 0
    while True:

        start = []
        for i in range(N):
            for j in range(M):
                if bingsan[i][j] > 0:
                    start.append((i, j))
        if not start:
            return 0

        count = 0
        visited = [[False] * M for _ in range(N)]
        melt_count = [[0] * M for _ in range(N)]
        for x, y in start:
            if visited[x][y]:
                continue
            stack = [(x, y)]
            visited[x][y] = True
            while stack:
                now_x, now_y = stack.pop()
                for go in range(4):
                    next_x = now_x + dx[go]
                    next_y = now_y + dy[go]
                    if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                        if bingsan[next_x][next_y] <= 0:
                            melt_count[now_x][now_y] += 1
                        else:
                            stack.append((next_x, next_y))
                            visited[next_x][next_y] = True
            count += 1
        for x, y in start:
            bingsan[x][y] = max(bingsan[x][y] - melt_count[x][y], 0)

        if count >= 2:
            return year
        year += 1


N, M = map(int, input().split())
bingsan = [list(map(int, input().split())) for _ in range(N)]
print(DFS())
