import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
count = [0]*(N+1)
for i in range(M):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0]):
        edges[arr[j]].append(arr[j+1])
        count[arr[j+1]] += 1

queue = deque()
result = []
for i in range(1, N+1):
    if count[i] == 0:
        queue.append(i)
        result.append(i)

while queue:
    now = queue.popleft()
    for next in edges[now]:
        count[next] -= 1
        if count[next] == 0:
            queue.append(next)
            result.append(next)
if len(result) != N:
    print(0)
else:
    print(*result, sep="\n")