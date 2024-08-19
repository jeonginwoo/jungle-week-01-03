# 9
# 17
# 1 2 5
# 1 3 1
# 3 2 3
# 2 6 1
# 2 4 4
# 4 3 7
# 4 5 9
# 4 6 1
# 5 3 2
# 5 8 5
# 6 5 7
# 6 7 3
# 7 8 3
# 8 7 2
# 7 9 4
# 8 9 1
# 7 5 1
# 1 9

"""
출처 : 백준
번호 : 1916
난이도 : 골드 5
제목 : 최소비용 구하기
"""

import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    cost = [float("inf")] * (N + 1)
    cost[start] = 0
    heap = [(0, start)]
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if current_cost > cost[current_node]:
            continue
        for edge_cost, next_node in edges[current_node]:
            next_cost = current_cost + edge_cost
            if cost[next_node] > next_cost:
                cost[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
    return cost[end]


N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append((C, B))
start, end = map(int, input().split())
print(dijkstra(start))
