"""
출처 : 백준
번호 : 10830
난이도 : 골드 4
제목 : 행렬 제곱
"""

import sys


def metrix(X, Y):
    global N
    Z = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z


def left(X, C):
    global N
    L = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            L[i][j] = X[i][j] % C
    return L


def power(A, B):
    if B == 0:
        return 1
    elif B == 1:
        return left(A, 1000)
    else:
        half = power(A, B // 2)
        if B % 2 == 0:
            return left(metrix(half, half), 1000)
        else:
            return left(metrix(metrix(half, half), A), 1000)


N, B = map(int, input().split())
A = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
metrix(A, A)
metrixA = power(A, B)
for i in range(N):
    for j in range(N):
        print(metrixA[i][j], end=" ")
    print()
