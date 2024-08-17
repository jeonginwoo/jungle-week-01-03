"""
출처 : 백준
번호 : 1260
난이도 : 실버 2
제목 : DFS와 BFS
"""

import sys
from collections import deque

def DFS(edges, V):
    visited = [False] * (len(edges) + 1)
    visit = []
    stack = [V]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            visit.append(v)
            stack += edges[v][::-1]
    return visit

def BFS(edges, V):
    visited = [False] * (len(edges) + 1)
    visit = []
    queue = deque()
    queue.append(V)
    while queue:
        v = queue.popleft()
        if not visited[v]:
            visited[v] = True
            visit.append(v)
            next_list = edges[v]
            for next in next_list:
                if not visited[next]:
                    queue.append(next)
    return visit

input = sys.stdin.readline

N, M, V = map(int, input().split())
edges = [[] for _ in range(N+1)]
for i in range(M):
    arr = list(map(int, input().split()))
    edges[arr[0]].append(arr[1])
    edges[arr[1]].append(arr[0])
for i in range(1, N+1):
    edges[i].sort()
print(*DFS(edges, V))
print(*BFS(edges, V))