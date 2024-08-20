"""
출처 : 백준
번호 : 2617
난이도 : 골드 4
제목 : 구슬 찾기
"""

import sys
input = sys.stdin.readline


def dfs():
    up_count = [0] * (N+1)
    down_count = [0] * (N+1)
    for i in range(1, N + 1):
        count = 0
        visited = [False]*(N+1)
        stack = [i]
        visited[i] = True
        while stack:
            now = stack.pop()
            for next in edges[now]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
                    up_count[next] += 1
                    count += 1
        down_count[i] = count

    count = 0
    for i in range(1, N+1):
        if down_count[i] >= mid or up_count[i] > N - mid:
            count += 1
    return count


N, M = map(int, input().split())
mid = (N + 1) // 2
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
print(dfs())
