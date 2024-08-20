"""
출처 : 백준
번호 : 1432
난이도 : 플래티넘 4
제목 : 그래프 수정
"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [[int(x) for x in input().strip()] for _ in range(N)]

edges = [[] for _ in range(N+1)]
count = [0] * (N+1)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            edges[j+1].append(i+1)
            count[i+1] += 1

exist = False
heap = []
for i in range(1, N + 1):
    if count[i] == 0:
        heapq.heappush(heap, -i)
        exist = True

num = N
result = [0] * (N+1)
while heap:
    now = -heapq.heappop(heap)
    result[now] = num
    num -= 1
    for next in edges[now]:
        count[next] -= 1
        if count[next] == 0:
            heapq.heappush(heap, -next)

if exist:
    print(*result[1:])
else:
    print(-1)
