"""
출처 : 백준
번호 : 14501
난이도 : 실버 3
제목 : 퇴사
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [0]+[list(map(int, input().split())) for _ in range(N)]

dp = [0]*(N+1)
dp[1] = arr[1][1]
for day in range(2, N+1):
    T, P = arr[day]
    if day + T <= N:
        dp[day + T] = max(dp[day + T], dp[day] + P)
print(dp)