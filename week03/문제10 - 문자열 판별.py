"""
출처 : 백준
번호 : 16500
난이도 : 골드 5
제목 : 문자열 판별
"""

S = input()
N = int(input())
A = [input() for _ in range(N)]

dp = [False] * (len(S) + 1)
dp[0] = True
for i in range(1, len(S) + 1):
    for j in range(i):
        if dp[j] and S[j:i] in A:
            dp[i] = True
            break

print(1 if dp[len(S)] else 0)