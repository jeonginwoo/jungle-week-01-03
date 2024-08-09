"""
출처 : 백준
번호 : 2750
난이도 : 브론즈 2
제목 : 수 정렬하기
"""


N = int(input())
numList = []
for _ in range(N):
    numList.append(int(input()))

numList.sort()
for num in numList:
    print(num)