"""
출처 : 백준
번호 : 2294
난이도 : 골드 5
제목 : 동전 2
"""

import sys
import heapq
input = sys.stdin.readline


n, k = map(int, input().split())

heap = []
coins = list(map(int, sys.stdin.read().split()))
visited = [False] * (k+1)

heapq.heappush(heap, (0, k))
visited[k] = True
result = -1
while heap:
    count, now = heapq.heappop(heap)
    if now == 0:
        result = count
        break
    for next in coins:
        value = now - next
        if value >= 0 and not visited[value]:
            heapq.heappush(heap, (count+1, value))
            visited[value] = True

print(result)
