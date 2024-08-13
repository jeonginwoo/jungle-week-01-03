"""
출처 : 백준
번호 : 1629
난이도 : 실버 1
제목 : 곱셈
"""

import sys


def multi(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C
    else:
        half = multi(A, B // 2, C)
        if B % 2 == 0:
            return (half ** 2) % C
        else:
            return (half ** 2) * A % C


A, B, C = map(int, sys.stdin.readline().split())
print(multi(A, B, C))
