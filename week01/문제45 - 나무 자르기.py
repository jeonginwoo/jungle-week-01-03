"""
출처 : 백준
번호 : 1920
난이도 : 실버 4
제목 : 수 찾기
"""

import math

N, M = [int(x) for x in input().split()]
heightList = sorted([int(x) for x in input().split()], reverse=True) + [0]

count = 0
sumHeight = 0
for i in range(N):
    count += 1
    if heightList[i] == heightList[i + 1]:
        continue
    sumHeight += (heightList[i] - heightList[i + 1]) * count
    if sumHeight >= M:
        preSumHeight = sumHeight - (heightList[i] - heightList[i + 1]) * count
        leftHeight = M - preSumHeight
        print(heightList[i] - math.ceil(leftHeight / count))
        break
