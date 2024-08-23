"""
출처 : 백준
번호 : 1463
난이도 : 실버 3
제목 : 1로 만들기
"""

N = int(input())
dp = [0] * (N + 1)
for num in range(2, N + 1):
    dp[num] = dp[num - 1] + 1
    if num % 2 == 0:
        dp[num] = min(dp[num], dp[num // 2] + 1)
    if num % 3 == 0:
        dp[num] = min(dp[num], dp[num // 3] + 1)

print(dp[N])
