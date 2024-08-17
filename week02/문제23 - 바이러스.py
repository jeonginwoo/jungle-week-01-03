"""
출처 : 백준
번호 : 2606
난이도 : 실버 3
제목 : 바이러스
"""

import sys


def DFS(edges):
    visited = [False] * (len(edges) + 1)
    count = 0
    stack = [1]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            count += 1
            stack += edges[v][::-1]
    return count - 1


input = sys.stdin.readline
N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    arr = list(map(int, input().split()))
    edges[arr[0]].append(arr[1])
    edges[arr[1]].append(arr[0])
print(DFS(edges))
