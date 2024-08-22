"""
출처 : 백준
번호 : 1904
난이도 : 실버 3
제목 : 01타일
"""

import sys
input = sys.stdin.readline


N = int(input())

if N == 1:
    print(1)
    quit()
elif N == 2:
    print(2)
    quit()
dp = [None]*(N)
dp[0] = 1
dp[1] = 2
for i in range(2, N):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[-1])