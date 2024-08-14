"""
출처 : 백준
번호 : 1920
난이도 : 실버 4
제목 : 수 찾기
"""


def checkNum(find, numList):
    start = 0
    end = len(numList) - 1
    while start != end:
        now = (start + end) // 2
        if numList[now] < find:
            start = now + 1
        elif numList[now] > find:
            end = now
        else:
            start = end = now
    if find == numList[start]:
        print(1)
    else:
        print(0)


N = int(input())
numList = sorted([int(x) for x in input().split()])
M = int(input())
checkList = [int(x) for x in input().split()]

for num in checkList:
    checkNum(num, numList)
