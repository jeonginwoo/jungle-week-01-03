"""
출처 : 백준
번호 : 2750
난이도 : 브론즈 2
제목 : 수 정렬하기
"""

import sys

sys.setrecursionlimit(15000)


def quickSort(numList, first, last):
    if first >= last:
        return
    p = numList[first]
    left = first + 1
    right = last
    while left <= right:
        while left <= right and numList[left] < p:
            left += 1
        while numList[right] > p:
            right -= 1
        if left <= right:
            numList[left], numList[right] = numList[right], numList[left]
            left += 1
            right -= 1
    numList[first], numList[right] = numList[right], numList[first]
    quickSort(numList, first, right - 1)
    quickSort(numList, left, last)


N = int(input())
numList = []
for _ in range(N):
    numList.append(int(input()))
quickSort(numList, 0, N - 1)
for num in numList:
    print(num)
