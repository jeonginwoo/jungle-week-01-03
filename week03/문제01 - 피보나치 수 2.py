"""
출처 : 백준
번호 : 2748
난이도 : 브론즈 1
제목 : 피보나치 수 2
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [None] * (N + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1])
