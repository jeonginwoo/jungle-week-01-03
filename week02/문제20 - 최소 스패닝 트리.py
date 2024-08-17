"""
출처 : 백준
번호 : 1197
난이도 : 골드 4
제목 : 최소 스패닝 트리
"""

import sys


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def checkSame(a, b):
    if find(a) == find(b):
        return True
    return False


input = sys.stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
parent = [x for x in range(V + 1)]

weight = 0
for edge in edges:
    if not checkSame(edge[0], edge[1]):
        union(edge[0], edge[1])
        weight += edge[2]
print(weight)
