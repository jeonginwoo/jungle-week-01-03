"""
출처 : 백준
번호 : 2470
난이도 : 골드 5
제목 : 두 용액
"""

import sys

lines = sys.stdin.read().splitlines()
N = int(lines[0])
arr = sorted([int(x) for x in lines[1].split()])

minSum = float("inf")
minLeft = 0
minRight = N-1

for i in range(N - 1):
    start = i + 1
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        sum = arr[i] + arr[mid]
        if minSum > abs(sum):
            minSum = abs(sum)
            minLeft = arr[i]
            minRight = arr[mid]
        if sum < 0:
            start = mid + 1
        elif sum > 0:
            end = mid - 1
        else:
            break
print(minLeft, minRight)

