"""
출처 : 백준
번호 : 10819
난이도 : 실버 2
제목 : 차이를 최대로
"""


def diffSum(numList):
    sum = 0
    for i in range(len(numList) - 1):
        sum += abs(numList[i] - numList[i + 1])
    return sum


def maxOrder(n, numList, shuf, maxSum):
    if n == 0:
        maxSum[0] = max(maxSum[0], diffSum(shuf))
        return
    for num in range(len(numList)):
        tempNumList = numList[:]
        tempShuf = shuf[:]
        tempShuf.append(tempNumList.pop(num))
        maxOrder(n - 1, tempNumList, tempShuf, maxSum)


N = int(input())
numList = [int(x) for x in input().split()]

temp = numList[:]
shuf = []
maxSum = [0]
maxOrder(N, numList, shuf, maxSum)
print(maxSum[0])
