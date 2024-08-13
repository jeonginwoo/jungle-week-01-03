"""
출처 : 백준
번호 : 10971
난이도 : 실버 2
제목 : 외판원 순회 2
"""

import sys


def dfs(now, dist, i):
    global N, W, cityList, visited, firstCity, minDist
    if i == 0:
        for city in cityList:
            visited[city] = True
            firstCity = city
            dfs(city, 0, i + 1)
    else:
        if i == N:
            if W[now][firstCity] != 0:
                minDist = min(minDist, dist + W[now][firstCity])
        for next in cityList:
            if not visited[next] and W[now][next] != 0:
                visited[next] = True
                dfs(next, dist + W[now][next], i + 1)
                visited[next] = False


N = int(input())
lines = sys.stdin.read().splitlines()
W = [list(map(int, line.split())) for line in lines]

cityList = [x for x in range(N)]
visited = [False] * N
firstCity = None
minDist = float("inf")

dfs(None, 0, 0)
print(minDist)
