"""
출처 : 백준
번호 : 16564
난이도 : 실버 1
제목 : 히오스 프로게이머
"""

N, K = [int(x) for x in input().split()]
X_list = []
for _ in range(N):
    X_list.append(int(input()))
X_list.sort()

sumLevel = 0
nowLevel = X_list[0]
count = 1
for i in range(N - 1):
    if X_list[i] == X_list[i + 1]:
        count += 1
        continue
    sumLevel += (X_list[i + 1] - X_list[i]) * count
    if sumLevel >= K:
        sumLevel -= (X_list[i + 1] - X_list[i]) * count
        break
    nowLevel = X_list[i + 1]
    count += 1

leftLevel = K - sumLevel
nowLevel += leftLevel // count
print(nowLevel)
