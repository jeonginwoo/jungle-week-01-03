"""
출처 : 백준
번호 : 1707
난이도 : 골드 4
제목 : 이분 그래프
"""

import sys


def DFS(start):
    global V, edges, colors
    stack = [start]
    colors[start] = "A"
    while stack:
        now = stack.pop()
        for next in edges[now]:
            if colors[next] == colors[now]:
                return False
            if colors[next] is None:
                stack.append(next)
                colors[next] = "B" if colors[now] == "A" else "A"
    return True


input = sys.stdin.readline
K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]
    for j in range(E):
        arr = list(map(int, input().split()))
        edges[arr[0]].append(arr[1])
        edges[arr[1]].append(arr[0])
    count = 0
    colors = [None] * (V + 1)
    for start in range(1, V + 1):
        if colors[start] is None and not DFS(start):
            count += 1
            break
    print("YES" if count == 0 else "NO")
