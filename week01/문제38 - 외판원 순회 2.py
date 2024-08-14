"""
출처 : 백준
번호 : 10971
난이도 : 실버 2
제목 : 외판원 순회 2
"""

import sys


def travel(i, now, cost):
    global N, W, first_city, visited, minCost

    if i == N:
        if W[now][first_city] != 0:
            minCost = min(minCost, cost + W[now][first_city])
        return

    for next in range(N):
        if i == 0:
            first_city = next
            visited[next] = True
            travel(i + 1, next, 0)
            visited[next] = False
        else:
            if not visited[next] and W[now][next] != 0:
                visited[next] = True
                travel(i + 1, next, cost + W[now][next])
                visited[next] = False


N = int(input())
W = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
first_city = None
visited = [False] * N
minCost = float('inf')
travel(0, None, 0)
print(minCost)

