"""
출처 : 백준
번호 : 1074
난이도 : 실버 1
제목 : Z
"""


def Z(N, x, y):
    global count, r, c
    nextX = x - 2 ** (N - 1)
    nextY = y - 2 ** (N - 1)

    if r <= nextX and c <= nextY:
        if N == 1:
            return 0
        return Z(N - 1, nextX, nextY)
    elif r <= nextX and c > nextY:
        if N == 1:
            return 1
        return Z(N - 1, nextX, y) + 4 ** (N - 1)
    elif r > nextX and c <= nextY:
        if N == 1:
            return 2
        return Z(N - 1, x, nextY) + 2 * 4 ** (N - 1)
    else:
        if N == 1:
            return 3
        return Z(N - 1, x, y) + 3 * 4 ** (N - 1)


N, r, c = [int(x) for x in input().split()]
count = 0
print(Z(N, x=2 ** N - 1, y=2 ** N - 1))
