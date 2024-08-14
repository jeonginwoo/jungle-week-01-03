"""
출처 : 백준
번호 : 2261
난이도 : 플래티넘 2
제목 : 가장 가까운 두 점
"""

import sys


def dotDist(dot1, dot2):
    return (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2


def partMinDist(left, right):
    global dot_list

    min_dist = float("inf")
    for i in range(left, right):
        for j in range(i + 1, right + 1):
            min_dist = min(min_dist, dotDist(dot_list[i], dot_list[j]))
    return min_dist


def minDist(left, right):
    global dot_list

    if right - left + 1 <= 3:
        return partMinDist(left, right)
    mid = (left + right) // 2
    min_dist = min(minDist(left, mid), minDist(mid + 1, right))

    div_x = (dot_list[mid][0] + dot_list[mid + 1][0]) / 2
    mid_dot_list = []
    for i in range(left, right + 1):
        if (dot_list[i][0] - div_x) ** 2 <= min_dist:
            mid_dot_list.append(dot_list[i])
    mid_dot_list.sort(key=lambda x: x[1])

    n = len(mid_dot_list)
    mid_min_dist = float("inf")
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (mid_dot_list[i][1] - mid_dot_list[j][1]) ** 2 >= min_dist:
                break
            mid_min_dist = min(mid_min_dist, dotDist(mid_dot_list[i], mid_dot_list[j]))
    min_dist = min(min_dist, mid_min_dist)

    return min_dist


n = int(input())
dot_list = sorted([list(map(int, line.split())) for line in sys.stdin.read().splitlines()])
print(minDist(0, n - 1))
