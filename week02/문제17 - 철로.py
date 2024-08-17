"""
출처 : 백준
번호 : 1715
난이도 : 골드 4
제목 : 카드 정렬하기
"""

import heapq
import sys

input = sys.stdin.readline

n = int(input())
a = [sorted(list(map(int, input().split()))) for _ in range(n)]
d = int(input())

arr = []
for i in range(n):
    if a[i][1] - a[i][0] <= d:
        arr.append(a[i])
arr.sort(key=lambda x: (x[1], x[0]))

heap = []
max_count = 0
count = 0
for i in range(len(arr)):
    now = arr[i][1]
    while heap and heap[0][0] < now-d:
        heapq.heappop(heap)
        count -= 1
    heapq.heappush(heap, arr[i])
    count += 1
    max_count = max(max_count, count)
print(max_count)
