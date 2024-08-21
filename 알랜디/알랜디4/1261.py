import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    count = 0
    temp = []
    while queue:
        now_x, now_y = queue.popleft()
        for go in range(4):
            next_x = now_x + dx[go]
            next_y = now_y + dy[go]
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                if next_x == N-1 and next_y == M-1:
                    return count
                visited[next_x][next_y] = True
                if miro[next_x][next_y] == 0:
                    queue.append((next_x, next_y))
                else:
                    temp.append((next_x, next_y))
                    continue
        if not queue and temp:
            for x, y in temp:
                miro[x][y] = 0
            queue = deque(temp)
            temp = []
            count += 1
    return count


M, N = map(int, input().split())
miro = [[int(x) for x in input().strip()] for _ in range(N)]
print(bfs())



"""
지언 코드

import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
dx=[1,0,-1,0]
dy=[0,1,0,-1]

arr=[input().rstrip() for _ in range (M)]
visited=[[False]*N for _ in range (M)]
heap=[]

heapq.heappush(heap,(0,0,0))
visited[0][0]=True

while heap:
    cost,x,y=heapq.heappop(heap)
    if x==N-1 and y==M-1:
        print(cost)
        break;
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue;
        if visited[ny][nx]:
            continue
        visited[ny][nx]=True
        heapq.heappush(heap,(cost+int(arr[ny][nx]),nx,ny))
"""