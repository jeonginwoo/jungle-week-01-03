"""
출처 : 백준
번호 : 18352
난이도 : 실버 2
제목 : 특정 거리의 도시 찾기
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS(X):
    global N, K, edges
    visited = [False] * (N + 1)
    visit = []
    queue = deque()
    queue.append(X)
    visited[X] = True
    while queue:
        now = queue.popleft()
        for next in edges[now]:
            if not visited[next]:
                visited[next] = True
                count[next] = count[now] + 1
                if count[next] == K:
                    visit.append(next)
                    continue
                queue.append(next)
    return visit


N, M, K, X = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
count = [0] * (N + 1)
visit = BFS(X)
visit.sort()
if visit:
    for v in visit:
        print(v)
else:
    print(-1)
