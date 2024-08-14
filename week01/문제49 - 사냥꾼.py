"""
출처 : 백준
번호 : 8983
난이도 : 골드 4
제목 : 사냥꾼
"""

import sys


def area(animal):
    global L
    if animal[1] <= L:
        left = L - animal[1]
        return [animal[0] - left, animal[0] + left]
    return None


lines = sys.stdin.read().splitlines()
M, N, L = map(int, lines[0].split())
H = sorted(list(map(int, lines[1].split())))
A = [list(map(int, line.split())) for line in lines[2:]]

count = 0
for animal in A:
    hunt_area = area(animal)
    if hunt_area != None:
        start = 0
        end = M - 1
        while start <= end:
            mid = (start + end) // 2
            if H[mid] < hunt_area[0]:
                start = mid + 1
            elif H[mid] > hunt_area[1]:
                end = mid - 1
            else:
                count += 1
                break
print(count)
