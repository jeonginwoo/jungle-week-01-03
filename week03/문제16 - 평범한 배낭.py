"""
출처 : 백준
번호 : 12865
난이도 : 골드 5
제목 : 평범한 배낭
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)
for weight, value in info:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[K])
