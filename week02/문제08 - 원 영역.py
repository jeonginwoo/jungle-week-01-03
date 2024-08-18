"""
출처 : 백준
번호 : 10000
난이도 : 플래티넘 4
제목 : 원 영역
"""

import sys
from collections import deque

input = sys.stdin.readline


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
    check = circle_list[i][1]
    while len(stack) > 0:
        if check <= circle_list[stack[-1]][1]:
            stack.append(i)
            return stack[-2]
        stack.pop()


N = int(input())
# 원 입력을 x좌표 구간으로 변경
circle_list = [[c[0] - c[1], c[0] + c[1]] for c in (list(map(int, input().split())) for i in range(N))]
# 구간 왼쪽에 대해서 오름차순, 구간 오른쪽에 대해서 내림차순으로 정렬
circle_list.sort(key=lambda x: (x[0], -x[1]))
# 정렬된 리스트의 인덱스가 각 원의 번호 (0번은 전체 구간)
circle_list = [[-float("inf"), float("inf")]] + circle_list

edges = [[] for _ in range(N + 1)]
stack = [0]
for i in range(1, N + 1):
    edges[find(i)].append(i)
print(BFS())
