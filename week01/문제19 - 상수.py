"""
출처 : 백준
번호 : 2908
난이도 : 브론즈 2
제목 : 상수
"""

def newNum(num):
    new = 0
    while num > 0:
        new = new * 10 + num % 10
        num //= 10
    return new

A, B = [int(x) for x in input().split()]
print(max(newNum(A), newNum(B)))

