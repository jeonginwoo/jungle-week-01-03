"""
출처 : 백준
번호 : 12852
난이도 : 실버 1
제목 : 1로 만들기
"""

import sys
input = sys.stdin.readline

N = int(input())

dp = [float("inf")]*(N+1)
dp[N] = 0
memo = [0] * (N + 1)
for x in range(N-1, 0, -1):
    min_count = None
    case = []
    case3 = [dp[x*3] if x*3 <=N else float("inf"), 3]
    case2 = [dp[x*2] if x*2 <=N else float("inf"), 2]
    case1 = [dp[x+1], 1]
    if case1 < case2:
        min_count = case1
        memo[x] = 1
    else:
        min_count = case2
        memo[x] = 2
    if case3 < min_count:
        min_count = case3
        memo[x] = 3
    dp[x] = min_count+1

i=1
result = []
while i<N:
    result.append(i)
    if memo[i] == 1:
        i += 1
    else:
        i *= memo[i]
result.append(N)

print(dp[1])
print(*result[::-1])