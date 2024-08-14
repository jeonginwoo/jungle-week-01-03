"""
출처 : 백준
번호 : 2470
난이도 : 골드 5
제목 : 두 용액
"""

import sys

lines = sys.stdin.read().splitlines()
N = int(lines[0])
X = sorted(list(map(int, lines[1].split())))

liquid = [None, None]
minMix = float('inf')
for i in range(N - 1):
    start = i + 1
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        mix = X[i] + X[mid]
        if minMix > abs(mix):
            minMix = abs(mix)
            liquid[0] = X[i]
            liquid[1] = X[mid]
        if mix < 0:
            start = mid + 1
        elif mix > 0:
            end = mid - 1
        else:
            break
print(liquid[0], liquid[1])

