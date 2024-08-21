import sys
input = sys.stdin.readline


def dfs():
    count = n
    visited = [False] * (n+1)
    start = [x for x in range(1, n+1)]
    a = []
    for s in start:
        if not visited[s]:
            stack = [s]
            visited[s] = True
            while stack:
                now = stack.pop()
                next = edges[now]
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
                else:
                    visited2 = [False] * (n+1)
                    while not visited2[next] and now != next:
                        next = edges[next]
                        visited2[next] = True
                        count -= 1
                    if now == next:
                        count -= 1
    return count

T = int(input())
for _ in range(T):
    n = int(input())
    edges = [0 for _ in range(n+1)]
    arr = list(map(int, input().split()))
    for i in range(1, n+1):
        edges[i] = arr[i-1]
    print(dfs())
    print()