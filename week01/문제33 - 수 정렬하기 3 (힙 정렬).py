"""
출처 : 백준
번호 : 10989
난이도 : 브론즈 1
제목 : 수 정렬하기 3
"""

# 메모리 초과

import heapq
import sys

input = sys.stdin.read


def heapSort(numList):
    heapq.heapify(numList)
    sortedList = []
    while len(numList) > 0:
        sortedList.append(heapq.heappop(numList))
    return sortedList


data = input().split()
N = int(data[0])
numList = list(map(int, data[1:]))

sortedList = heapSort(numList)
for num in sortedList:
    print(num)
