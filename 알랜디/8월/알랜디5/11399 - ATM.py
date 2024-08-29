"""
출처 : 백준
번호 : 14501
난이도 : 실버 3
제목 : ATM
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
j = N
for i in range(N):
    result += arr[i]*j
    j-=1
print(result)