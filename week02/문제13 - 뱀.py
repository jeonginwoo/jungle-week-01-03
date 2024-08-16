"""
출처 : 백준
번호 : 3190
난이도 : 골드 4
제목 : 뱀
"""

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
rotate = [[int(r[0]), r[1]] for r in [input().split() for _ in range(L)]]

board = [[False] * N for _ in range(N)]
board[0][0] = True
snake = deque()
snake.append([1, 1])

go_x = [0, 1, 0, -1]
go_y = [1, 0, -1, 0]
go = 0

i = 0   # 방향
time = 0
while True:
    if i < L and time == rotate[i][0]:
        go = go + 1 if rotate[i][1] == 'D' else go - 1
        i += 1

    head = snake[-1][:]
    head[0] += go_x[go % 4]
    head[1] += go_y[go % 4]
    if not (1 <= head[0] <= N) or not (1 <= head[1] <= N) or board[head[0]-1][head[1]-1]:
        time += 1
        break

    if len(apple) > 0 and head in apple:
        apple.remove(head)
    else:
        tail = snake.popleft()
        board[tail[0]-1][tail[1]-1] = False
    snake.append(head)
    board[head[0]-1][head[1]-1] = True

    time += 1

    # for a in range(N):
    #     for b in range(N):
    #         print("{:2b}".format(board[a][b]), end="")
    #     print()
    # print()

print(time)