"""
출처 : 백준
번호 : 10950
난이도 : 브론즈 5
제목 : A+B - 3
"""

N = int(input())
for i in range(N):
    a, b = [int(x) for x in input().split()]
    print(a + b)