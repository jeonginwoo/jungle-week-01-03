"""
출처 : 백준
번호 : 1912
난이도 : 실버 2
제목 : 연속합
"""

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0]*n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print(max(dp))