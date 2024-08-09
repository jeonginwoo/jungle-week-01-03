"""
출처 : 백준
번호 : 10872
난이도 : 브론즈 3
제목 : 팩토리얼
"""


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


N = int(input())
print(factorial(N))