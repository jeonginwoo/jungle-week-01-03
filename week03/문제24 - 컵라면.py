"""
출처 : 백준
번호 : 1781
난이도 : 골드 2
제목 : 컵라면
"""

import sys, heapq
input = sys.stdin.readline

N = int(input())
cups = [list(map(int, input().split())) for _ in range(N)]
cups.sort()

heap = []
day = 0
for deadline, num in cups:
    heapq.heappush(heap, num)
    if deadline < len(heap):
        heapq.heappop(heap)
print(sum(heap))