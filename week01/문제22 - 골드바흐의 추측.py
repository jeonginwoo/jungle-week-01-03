"""
출처 : 백준
번호 : 9020
난이도 : 실버 2
제목 : 골드바흐의 추측
"""

T = int(input())
isPrime = [False, False] + [True] * (10000 - 1)
for num in range(2, 10001):
    if isPrime[num]:
        i = 2
        while num*i <= 10000:
            isPrime[num * i] = False
            i += 1

for _ in range(T):
    num = int(input())
    half = num//2

    prime1 = 0
    prime2 = 0
    gold1 = 2
    while gold1 <= half:
        gold2 = num - gold1
        if isPrime[gold1] and isPrime[gold2]:
            prime1 = gold1
            prime2 = gold2
        gold1 += 1
    print(prime1, prime2)