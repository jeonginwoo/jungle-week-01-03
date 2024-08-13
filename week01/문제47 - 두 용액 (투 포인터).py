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

left = 0
right = N-1
while left < right:
    sum = arr[left] + arr[right]
    if minSum > abs(sum):
        minSum = abs(sum)
        minLeft = left
        minRight = right
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        break
print(arr[minLeft], arr[minRight])