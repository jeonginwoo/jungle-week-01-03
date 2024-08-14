"""
출처 : 백준
번호 : 14888
난이도 : 실버 1
제목 : 연산자 끼워넣기
"""

import sys


def dfs(i, result):
    global N, A_list, count, maxResult, minResult

    if i == N:
        maxResult = max(maxResult, result)
        minResult = min(minResult, result)
        return
    else:
        if count[0] > 0:
            count[0] -= 1
            dfs(i + 1, result + A_list[i])
            count[0] += 1
        if count[1] > 0:
            count[1] -= 1
            dfs(i + 1, result - A_list[i])
            count[1] += 1
        if count[2] > 0:
            count[2] -= 1
            dfs(i + 1, result * A_list[i])
            count[2] += 1
        if count[3] > 0:
            count[3] -= 1
            dfs(i + 1, int(result / A_list[i]))
            count[3] += 1


lines = sys.stdin.read().splitlines()
N = int(lines[0])
A_list = list(map(int, lines[1].split()))
count = list(map(int, lines[2].split()))
maxResult = -float("inf")
minResult = float("inf")
dfs(1, A_list[0])
print(maxResult)
print(minResult)
