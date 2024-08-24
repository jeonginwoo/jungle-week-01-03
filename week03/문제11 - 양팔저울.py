"""
출처 : 백준
번호 : 2629
난이도 : 골드 3
제목 : 양팔저울
"""


A = int(input())
Aw = list(map(int, input().split()))
B = int(input())
Bw = list(map(int, input().split()))

max_x = sum(Aw)
# dp[i][j] : 첫 번째 추부터 i번째 추까지 고려했을 때 j 무게를 만들 수 있는지
dp = [[False] * (max_x + 1) for _ in range(A + 1)]
dp[0][0] = True

for i in range(1, A + 1):
    for j in range(max_x+1):
        if dp[i - 1][j]:
            dp[i][j] = True
            dp[i][j + Aw[i - 1]] = True
            dp[i][abs(j - Aw[i - 1])] = True

result = []
for weight in Bw:
    if weight > max_x:
        result.append("N")
    else:
        result.append("Y" if dp[A][weight] else "N")

print(*result)
