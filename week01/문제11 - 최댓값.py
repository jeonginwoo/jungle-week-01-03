"""
출처 : 백준
번호 : 2562
난이도 : 브론즈 3
제목 : 최댓값
"""

maxNum = int(input())
maxIdx = 1
for i in range(2, 10):
    nowNum = int(input())
    if maxNum < nowNum:
        maxNum = nowNum
        maxIdx = i
print(maxNum)
print(maxIdx)