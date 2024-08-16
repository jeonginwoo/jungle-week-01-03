"""
출처 : 백준
번호 : 1655
난이도 : 골드 2
제목 : 가운데를 말해요
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
say = list(map(int, sys.stdin.read().split()))

max_heap = []
min_heap = []
for i in range(N):
    if len(max_heap) <= len(min_heap):
        heapq.heappush(max_heap, -say[i])
    else:
        heapq.heappush(min_heap, say[i])
    if i > 0 and -max_heap[0] > min_heap[0]:
        left = -heapq.heappop(max_heap)
        right = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -right)
        heapq.heappush(min_heap, left)
    print(-max_heap[0])