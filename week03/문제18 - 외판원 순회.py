"""
출처 : 백준
번호 : 12920
난이도 : 골드 1
제목 : 외판원 순회
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(now, visited):
    if visited == (1 << N) - 1:
        return W[now][0] if W[now][0] else float("inf")

    if (now, visited) in dp:
        return dp[(now, visited)]

    for next in range(1, N):
        if W[now][next] == 0 or visited & (1 << next):
            continue
        dp[(now, visited)] = min(dp[(now, visited)], dfs(next, visited|1<<next) + W[now][next])

    return dp[(now, visited)]


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
# dp[(n, v)] : n번 도시, 방문 상태가 v일 때 최소 비용
dp = defaultdict(lambda: float("inf"))

print(dfs(0, 1))
