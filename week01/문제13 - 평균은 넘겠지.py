"""
출처 : 백준
번호 : 4344
난이도 : 브론즈 1
제목 : 평균은 넘겠지
"""

N = int(input())
for i in range(N):
    pointList = [int(x) for x in input().split()]
    average = (sum(pointList) - pointList[0]) / pointList[0]
    num = 0
    for j in range(1, pointList[0] + 1):
        if pointList[j] > average:
            num += 1
    print("{:.3f}%".format(num*100/pointList[0]))