"""
출처 : 백준
번호 : 1920
난이도 : 실버 4
제목 : 수 찾기
"""

N = int(input())
numSet = set([int(x) for x in input().split()])
M = int(input())
checkList = [int(x) for x in input().split()]

for num in checkList:
    if num in numSet:
        print(1)
    else:
        print(0)
