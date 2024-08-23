"""
출처 : 백준
번호 : 9084
난이도 : 골드 5
제목 : 동전
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [1] + [0] * (M)
    for coin in coins:
        for val in range(1, M+1):
            if val - coin >= 0:
                dp[val] += dp[val-coin]
    print(dp[M])