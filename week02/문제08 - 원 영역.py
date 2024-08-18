"""
출처 : 백준
번호 : 10000
난이도 : 플래티넘 4
제목 : 원 영역
"""

import sys
from collections import deque

input = sys.stdin.readline


def DFS():
    stack = [0]
    count = 1
    while stack:
        now = stack.pop()
        width = circle_list[now][1] - circle_list[now][0]
        child_width = 0
        for child in edges[now]:
            stack.append(child)
            count += 1
            child_width += circle_list[child][1] - circle_list[child][0]
        if width == child_width:
            count += 1
    return count


def BFS():
    queue = deque()
    queue.append(0)
    count = 1
    while queue:
        now = queue.popleft()
        width = circle_list[now][1] - circle_list[now][0]
        child_width = 0
        for child in edges[now]:
            queue.append(child)
            count += 1
            child_width += circle_list[child][1] - circle_list[child][0]
        if width == child_width:
            count += 1
    return count


# 부모 찾기
def find(i):
    global parent_stack, circle_list
    check = circle_list[i][1]
    while len(parent_stack) > 0:
        if check <= circle_list[parent_stack[-1]][1]:
            parent_stack.append(i)
            return parent_stack[-2]
        parent_stack.pop()


N = int(input())
circle_list = [[c[0] - c[1], c[0] + c[1]] for c in (list(map(int, input().split())) for i in range(N))]
circle_list.sort(key=lambda x: (x[0], -x[1]))
circle_list = [[-float("inf"), float("inf")]] + circle_list

edges = [[] for _ in range(N + 1)]
parent_stack = [0]
for i in range(1, N + 1):
    edges[find(i)].append(i)
# print(BFS())
print(DFS())
