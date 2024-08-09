"""
출처 : 백준
번호 : 2798
난이도 : 브론즈 2
제목 : 블랙잭
"""

N, M = [int(x) for x in input().split()]
cardList = [int(x) for x in input().split()]

maxSum = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            cardSum = cardList[i] + cardList[j] + cardList[k]
            if maxSum < cardSum <= M:
                maxSum = cardSum
print(maxSum)
