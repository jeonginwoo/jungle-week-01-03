"""
출처 : 백준
번호 : 11279
난이도 : 실버 2
제목 : 최대 힙
"""

import heapq
import sys
input = sys.stdin.readline


N = int(input())
max_heap = []
for _ in range(N):
    num = int(input())
    if num == 0:
        print(0 if len(max_heap) == 0 else -heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -num)

