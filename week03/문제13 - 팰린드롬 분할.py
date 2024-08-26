"""
출처 : 백준
번호 : 1509
난이도 : 골드 1
제목 : 팰린드롬 분할
"""

import sys
input = sys.stdin.readline

string = input().strip()
N = len(string)

is_palindrome = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        left, right = j - i, j
        if i == 0 or (i == 1 and string[left] == string[right]):
            is_palindrome[left][right] = True
            continue
        if string[left] == string[right] and is_palindrome[left + 1][right - 1]:
            is_palindrome[left][right] = True

dp = [float("inf") for _ in range(N)] + [0]
for right in range(N):
    for left in range(right + 1):
        print(f"({left}, {right})")
        print(string[left:right+1], end=" : ")
        if is_palindrome[left][right]:
            print("True")
            dp[right] = min(dp[right], dp[left - 1] + 1)
        else:
            print("False")
            dp[right] = min(dp[right], dp[right - 1] + 1)
        print(dp)
        print()
print(dp[N - 1])