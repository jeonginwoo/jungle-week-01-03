"""
출처 : 백준
번호 : 2750
난이도 : 브론즈 2
제목 : 수 정렬하기
"""

# 시간 초과

from collections import deque


def redixSort(numList, compareQueue):
    step = 1
    while True:
        for num in numList:
            compareQueue[(num // step) % 10].append(num)
        step *= 10
        if len(compareQueue[0]) == len(numList):
            break
        numList.clear()
        for i in range(10):
            while len(compareQueue[i]) != 0:
                numList.append(compareQueue[i].popleft())
    return


N = int(input())
numList = []
compareQueue = []
for i in range(10):
    compareQueue.append(deque())

for _ in range(N):
    numList.append(int(input()))
redixSort(numList, compareQueue)
for num in numList:
    print(num)
