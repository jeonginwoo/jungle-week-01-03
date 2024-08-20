"""
출처 : 백준
번호 : 1948
난이도 : 플래티넘 5
제목 : 임계경로
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n)]
count = [0] * n
for _ in range(m):
    start, end, time = map(int, input().split())
    edges[start - 1].append((end - 1, time))
    count[end - 1] += 1
start, end = map(int, input().split())

distance = [0] * n
road_count = [[] for _ in range(n)]
queue = deque([start-1])
while queue:
    now = queue.popleft()
    for next, dist in edges[now]:
        if distance[next] < distance[now] + dist:
            distance[next] = distance[now] + dist
            road_count[next] = [now]
        elif distance[next] == distance[now] + dist:
            road_count[next].append(now)
        count[next] -= 1
        if count[next] == 0:
            queue.append(next)

q = deque([end-1])
route = set()
while q:
    now = q.popleft()
    for x in road_count[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(distance[end-1])
print(len(route))