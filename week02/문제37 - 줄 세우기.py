"""
출처 : 백준
번호 : 2252
난이도 : 골드 3
제목 : 줄 세우기
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[] for _ in range(N + 1)]
count = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
    count[B] += 1
visit = []
queue = deque()
for start in range(1, N+1):
    if count[start] == 0:
        queue.append(start)
while queue:
    now = queue.popleft()
    visit.append(now)
    for next in edges[now]:
        count[next] -= 1
        if count[next] == 0:
            queue.append(next)
print(*visit)