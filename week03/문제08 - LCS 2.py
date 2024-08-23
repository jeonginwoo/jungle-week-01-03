"""
출처 : 백준
번호 : 9252
난이도 : 골드 4
제목 : LCS 2
"""

string1 = " " + input()
string2 = " " + input()

dp = [[0] * (len(string2)) for _ in range(len(string1))]
check = [[None] * (len(string2)) for _ in range(len(string1))]

for i in range(1, len(string1)):
    for j in range(1, len(string2)):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            check[i][j] = (-1, -1)
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                check[i][j] = (-1, 0)
            else:
                dp[i][j] = dp[i][j - 1]
                check[i][j] = (0, -1)

LCS = ""
i = len(string1) - 1
j = len(string2) - 1
while i > 0 and j > 0:
    x, y = check[i][j]
    if string1[i] == string2[j]:
        LCS += string1[i]
    i += x
    j += y

print(dp[-1][-1])
print(LCS[::-1])
