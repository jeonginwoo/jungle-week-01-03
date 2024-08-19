"""
출처 : 백준
번호 : 21606
난이도 : 골드 3
제목 : 아침 산책
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS():
    count = 0
    inside = []
    outside = []
    for i in range(1, N + 1):
        if A[i] == "1":
            inside.append(i)
        else:
            outside.append(i)

    visited_out = [False] * (N + 1)
    for out in outside:
        if not visited_out[out]:
            count_in = 0
            queue_in = deque([out])
            visited_out[out] = True
            while queue_in:
                now = queue_in.popleft()
                for next in edges[now]:
                    if not visited_out[next]:
                        if A[next] == "1":
                            count_in += 1
                        else:
                            queue_in.append(next)
                            visited_out[next] = True
            count += count_in * (count_in - 1)

    for now in inside:
        for next in edges[now]:
            if A[next] == "1":
                count += 1

    return count


N = int(input())
A = " " + input()
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    arr = list(map(int, input().split()))
    edges[arr[0]].append(arr[1])
    edges[arr[1]].append(arr[0])
print(BFS())
