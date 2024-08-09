"""
출처 : 백준
번호 : 1065
난이도 : 실버 4
제목 : 한수
"""

def isHansu(num):
    if num < 100:
        return True
    numList = []
    temp = num
    while temp > 0:
        numList.append(temp%10)
        temp//=10
    gong = numList[0] - numList[1]
    for i in range(1, len(numList)-1):
        if gong != numList[i] - numList[i+1]:
            return False
    return True

N = int(input())
count = 0
for num in range(1, N+1):
    if isHansu(num):
        count += 1
print(count)