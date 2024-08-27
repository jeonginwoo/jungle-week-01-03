"""
출처 : 백준
번호 : 2253
난이도 : 골드 4
제목 : 점프
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
small = set(int(x) - 1 for x in sys.stdin.read().splitlines())

max_v = int((2*N)**0.5)
dp = [[N] * (max_v+2) for _ in range(N)]
dp[0][0] = 0
for n in range(1, N):
    if n in small:
        continue
    for v in range(1, max_v+1):
        dp[n][v] = min(dp[n-v][v-1], dp[n-v][v], dp[n-v][v+1]) + 1
result = min(dp[N - 1])
print(result if result < N else -1)
