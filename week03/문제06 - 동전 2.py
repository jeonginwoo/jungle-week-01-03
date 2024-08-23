"""
출처 : 백준
번호 : 2294
난이도 : 골드 5
제목 : 동전 2
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set(list(map(int, sys.stdin.read().split())))
dp = [0] + [float("inf")] * k
for coin in coins:
    for val in range(1, k+1):
        if val - coin >= 0:
            dp[val] = min(dp[val], dp[val-coin] + 1)
print(dp[k] if dp[k] != float("inf") else -1)