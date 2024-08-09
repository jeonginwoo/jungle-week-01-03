"""
출처 : 백준
번호 : 2309
난이도 : 브론즈 1
제목 : 일곱 난쟁이
"""

heightList = []
for _ in range(9):
    heightList.append(int(input()))
heightList.sort()

allHeightSum = sum(heightList)
not1 = None
not2 = None
for i in range(8):
    for j in range(i+1, 9):
        heightSum = allHeightSum - heightList[i] - heightList[j]
        if (heightSum == 100):
            not1, not2 = i, j
            break

for i in range(9):
    if i == not1 or i == not2:
        continue
    print(heightList[i])