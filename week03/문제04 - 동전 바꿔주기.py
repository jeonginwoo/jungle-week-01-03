"""
출처 : 백준
번호 : 2624
난이도 : 골드 4
제목 : 동전 바꿔주기
"""

import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (T + 1)
dp[0] = 1

for coin, count in coins:
    for money in range(T, 0, -1):
        for i in range(1, count + 1):
            if money - coin * i >= 0:
                dp[money] += dp[money - coin * i]
print(dp[T])