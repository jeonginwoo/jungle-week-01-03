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
