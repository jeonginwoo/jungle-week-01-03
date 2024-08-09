"""
출처 : 백준
번호 : 9020
난이도 : 실버 2
제목 : 골드바흐의 추측
"""

T = int(input())
isDecimal = [False, False]+[True]*(10000 - 1)
for num in range(2, 10001):
    if isDecimal[num]:
        i = 2
        while num*i <= 10000:
            isDecimal[num*i] = False
            i += 1

for _ in range(T):
    num = int(input())
    half = num//2

    decimal1 = 0
    decimal2 = 0
    gold1 = 2
    while gold1 <= half:
        gold2 = num - gold1
        if isDecimal[gold1] and isDecimal[gold2]:
            decimal1 = gold1
            decimal2 = gold2
        gold1 += 1
    print(decimal1, decimal2)