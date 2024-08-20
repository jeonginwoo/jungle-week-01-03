"""
출처 : 백준
번호 : 6549
난이도 : 플래티넘 5
제목 : 히스토그램에서 가장 큰 직사각형
"""

import sys

input = sys.stdin.readline


def getPartArea(start, end):
    min_area = min(rect[start], rect[end - 1])
    max_area = max(rect[start], rect[end - 1])
    if end - start == 1:
        return rect[start]
    if end - start == 2:
        return max(max_area, min_area * 2)
    return -1


def getMaxArea(start, end):
    if end - start < 3:
        return getPartArea(start, end)
    mid = (start + end) // 2

    max_area = max(getMaxArea(start, mid), getMaxArea(mid, end))

    left = mid-1
    right = mid+1
    now_height = rect[mid]
    while start <= left and right < end:
        if rect[left] < rect[right]:
            if rect[right] < now_height:
                now_height = rect[right]
            max_area = max(max_area, now_height * (right - left))
            right += 1
        else:
            if rect[left] < now_height:
                now_height = rect[left]
            max_area = max(max_area, now_height * (right - left))
            left -= 1

    while start <= left:
        if rect[left] < now_height:
            now_height = rect[left]
        max_area = max(max_area, now_height * (right - left))
        left -= 1
    while right < end:
        if rect[right] < now_height:
            now_height = rect[right]
        max_area = max(max_area, now_height * (right - left))
        right += 1

    return max_area


while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0:
        break

    rect = arr[1:]
    start = 0
    end = n
    print(getMaxArea(start, end))
