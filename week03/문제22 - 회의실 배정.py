"""
출처 : 백준
번호 : 1931
난이도 : 실버 1
제목 : 회의실 배정
"""

import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
time.sort(key=lambda x: (x[1], x[0]))

count = 0
pre_end = 0
for t in time:
    start, end = t
    if pre_end <= start:
        pre_end = end
        count += 1
print(count)