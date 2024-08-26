"""
출처 : 백준
번호 : 11049
난이도 : 골드 3
제목 : 행렬 곱셈 순서
"""

# python3 시간 초과
# pypy3로 통과

import sys
input = sys.stdin.readline

N = int(input())
matrices = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]

dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(i, N):
        left, right = j - i, j
        dp[left][right] = float("inf")
        for k in range(left, right):
            dp[left][right] = min(dp[left][right], dp[left][k] + dp[k+1][right] + matrices[left][0] * matrices[k][1] * matrices[right][1])

print(dp[0][N - 1])