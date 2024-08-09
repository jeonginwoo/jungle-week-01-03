"""
출처 : 백준
번호 : 1978
난이도 : 브론즈 2
제목 : 소수 찾기
"""

def isPrime(num):
    if num == 1:
        return False
    div = 2
    half = num//2
    while div <= half:
        if num % div == 0:
            return False
        div += 1
    return True

n = int(input())
numList = [int(x) for x in input().split()]

count = 0
for num in numList:
    if isPrime(num):
        count += 1
print(count)