"""
출처 : 백준
번호 : 2193
난이도 : 실버 3
제목 : 이친수
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0] for _ in range(N+1)]
dp[1][1] = 1
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(sum(dp[N]))
