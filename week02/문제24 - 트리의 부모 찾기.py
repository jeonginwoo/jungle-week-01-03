"""
출처 : 백준
번호 : 11725
난이도 : 실버 2
제목 : 트리의 부모 찾기
"""

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
parent = [0, 0] + [None] * (N - 1)
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    arr = list(map(int, input().split()))
    edges[arr[0]].append(arr[1])
    edges[arr[1]].append(arr[0])

queue = deque()
visited = [False] * (N+1)
parent = [None] * (N+1)
queue.append(1)
while queue:
    v = queue.popleft()
    visited[v] = True
    for next in edges[v]:
        if not visited[next]:
            queue.append(next)
            parent[next] = v
for i in range(2, N+1):
    print(parent[i])