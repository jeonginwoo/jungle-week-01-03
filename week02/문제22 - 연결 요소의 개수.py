"""
출처 : 백준
번호 : 11724
난이도 : 실버 2
제목 : 연결 요소의 개수
"""

import sys


def graphCount(edges):
    global N
    visited = [False] * (N + 1)
    count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            count += 1
            stack = [i]
            while stack:
                v = stack.pop()
                if not visited[v]:
                    visited[v] = True
                    stack += edges[v]
    return count


input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    arr = list(map(int, input().split()))
    edges[arr[0]].append(arr[1])
    edges[arr[1]].append(arr[0])
print(graphCount(edges))
