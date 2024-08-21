import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

heap = []

for deadline, cupNoodle in arr:
    heapq.heappush(heap, cupNoodle)
    if deadline < len(heap):
        heapq.heappop(heap)
print(sum(heap))
