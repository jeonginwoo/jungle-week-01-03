"""
출처 : 백준
번호 : 2577
난이도 : 브론즈 2
제목 : 숫자의 개수
"""

A = int(input())
B = int(input())
C = int(input())
num = A * B * C
countList = [0]*10
while num > 0:
    countList[num%10] += 1
    num //= 10

for i in countList:
    print(i)
