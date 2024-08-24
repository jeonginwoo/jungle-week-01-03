"""
출처 : 백준
번호 : 10942
난이도 : 골드 4
제목 : 팰린드롬?
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
Q = [list(map(int, input().split())) for _ in range(M)]

dp = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        left, right = j - i, j
        if i == 0 or (i == 1 and nums[left] == nums[right]):
            dp[left][right] = True
            continue
        if nums[left] == nums[right] and dp[left+1][right-1]:
            dp[left][right] = True

for area in Q:
    left, right = area[0]-1, area[1]-1
    print(1 if dp[left][right] else 0)

