"""
출처 : 백준
번호 : 2751
난이도 : 실버 5
제목 : 수 정렬하기 2
"""

import sys

input = sys.stdin.read

def mergeSort(numList):
    if len(numList) <= 1:
        return numList

    half = len(numList) // 2
    left = numList[:half]
    right = numList[half:]

    leftSorted = mergeSort(left)
    rightSorted = mergeSort(right)

    return merge(leftSorted, rightSorted)


def merge(left, right):
    i = j = 0
    sortedArr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArr.append(left[i])
            i += 1
        else:
            sortedArr.append(right[j])
            j += 1
    while i < len(left):
        sortedArr.append(left[i])
        i += 1
    while j < len(right):
        sortedArr.append(right[j])
        j += 1

    return sortedArr


numList = list(map(int, input().split()[1:]))
sorted_arr = mergeSort(numList)

for num in sorted_arr:
    print(num)
