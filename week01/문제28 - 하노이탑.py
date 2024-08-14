"""
출처 : 백준
번호 : 1914
난이도 : 골드 5
제목 : 하노이탑
"""


def hanoi(N, now, next):
    if N == 0:
        return
    hanoi(N - 1, now, 6 - now - next)
    print(now, next)
    hanoi(N - 1, 6 - now - next, next)


N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3)
