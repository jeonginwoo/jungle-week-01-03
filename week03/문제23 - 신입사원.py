"""
출처 : 백준
번호 : 1946
난이도 : 실버 1
제목 : 신입사원
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()

    count = 1
    min_point = A[0][1]
    for i in range(1, N):
        if A[i][1] < min_point:
            count += 1
            min_point = A[i][1]
    print(count)
