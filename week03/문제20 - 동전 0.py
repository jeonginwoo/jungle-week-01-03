"""
출처 : 백준
번호 : 11047
난이도 : 실버 4
제목 : 동전 0
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(map(int, sys.stdin.read().splitlines()))
count = 0

for i in range(N-1, -1, -1):
    if coins[i] > K:
        continue
    if K == 0:
        break
    count += K // coins[i]
    K = K % coins[i]

print(count)