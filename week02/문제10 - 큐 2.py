"""
출처 : 백준
번호 : 18258
난이도 : 실버 4
제목 : 큐 2
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(N):
    command = input().split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        print(-1 if len(queue) == 0 else queue.popleft())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command[0] == "front":
        print(-1 if len(queue) == 0 else queue[0])
    elif command[0] == "back":
        print(-1 if len(queue) == 0 else queue[-1])
