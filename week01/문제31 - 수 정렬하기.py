"""
출처 : 백준
번호 : 2750
난이도 : 브론즈 2
제목 : 수 정렬하기
"""


def quickSort(numList, first, last):
    p = numList[first]
    left = first + 1
    right = last
    while left <= right:

    return


N = int(input())
numList = []
for _ in range(N):
    numList.append(int(input()))

quickSort(numList)
for num in numList:
    print(num)
