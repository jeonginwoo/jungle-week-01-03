"""
출처 : 백준
번호 : 2169
난이도 : 골드 2
제목 : 로봇 조종하기
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-float("inf")] * M for _ in range(N)]
dp[0][0] = arr[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + arr[0][j]
for i in range(1, N):
    temp = [[None] * M, [None] * M]
    temp[0][0], temp[1][-1] = dp[i - 1][0] + arr[i][0], dp[i - 1][-1] + arr[i][-1]
    for j in range(1, M):
        temp[0][j] = max(temp[0][j - 1], dp[i - 1][j]) + arr[i][j]
        temp[1][M - j - 1] = max(temp[1][M - j], dp[i - 1][M - j - 1]) + arr[i][M - j - 1]
    for j in range(M):
        dp[i][j] = max(temp[0][j], temp[1][j])

print(dp[-1][-1])
