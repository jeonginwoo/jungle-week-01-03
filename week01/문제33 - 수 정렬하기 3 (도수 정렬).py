"""
출처 : 백준
번호 : 10989
난이도 : 브론즈 1
제목 : 수 정렬하기 3
"""

import sys

maxVal = 10000
count = [0] * (maxVal + 1)

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    count[int(input())] += 1

for num in range(1, maxVal + 1):
    for _ in range(count[num]):
        print(num)
