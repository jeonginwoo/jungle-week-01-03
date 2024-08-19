"""
출처 : 백준
번호 : 2637
난이도 : 골드 2
제목 : 장난감 조립
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
step = [0] * (N + 1)
count = [0] * (N) + [1]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    edges[X].append([Y, Z])
    step[Y] += 1

parts = []
queue = deque([N])
while queue:
    now = queue.popleft()
    for next, w in edges[now]:
        step[next] -= 1
        if step[next] == 0:
            queue.append(next)
        count[next] += count[now] * w
    if not edges[now]:
        parts.append([now, count[now]])
parts.sort()
for part in parts:
    print(*part)