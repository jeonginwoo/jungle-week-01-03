"""
출처 : 백준
번호 : 12920
난이도 : 플래티넘 4
제목 : 평범한 배낭 2
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
items = []

for i in range(N):
    V, C, K = map(int, input().split())
    count = 1
    while K > 0:
        current_count = min(K, count)
        items.append([V * current_count, C * current_count])
        K -= current_count
        count *= 2

dp = [0] * (M + 1)
for weight, satis in items:
    for w in range(M, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + satis)

print(dp[M])
