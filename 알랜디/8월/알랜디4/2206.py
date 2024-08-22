import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count = [[0]*M for _ in range(N)]
    temp = []
    wall = 0
    queue = deque([(0, 0)])
    count[0][0] += 1
    result1 = float("inf")
    result2 = float("inf")
    while queue:
        now_x, now_y = queue.popleft()
        for go in range(4):
            next_x = now_x + dx[go]
            next_y = now_y + dy[go]
            if 0 <= next_x < N and 0 <= next_y < M and count[next_x][next_y] == 0:
                if next_x == N-1 and next_y == M-1:
                    if wall == 0:
                        result1 = count[now_x][now_y] + 1
                    elif wall == 1:
                        result2 = count[now_x][now_y] + 1
                    break
                count[next_x][next_y] = count[now_x][now_y] + 1
                if H[next_x][next_y] == 0:
                    queue.append((next_x, next_y))
                else:
                    temp.append((next_x, next_y))
                    continue
        if not queue and temp:
            queue = deque(temp)
            temp = []
            wall += 1
            if wall >= 2:
                break
    if result1 == result2 == float("inf") and count[-1][-1] != 1:
        return -1
    if count[-1][-1] != 1:
        count[-1][-1] = min(result1, result2)
    return count[-1][-1]


N, M = map(int, input().split())
H = [[int(x) for x in input().strip()] for _ in range(N)]
print(bfs())
