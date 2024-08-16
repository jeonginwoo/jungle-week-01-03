"""
출처 : 백준
번호 : 2493
난이도 : 골드 5
제목 : 탑
"""

import sys
input = sys.stdin.readline

N = int(input())
top_list = list(map(int, input().split()))

stack = []
result = [0] * N
for i in range(N - 1, -1, -1):
    while len(stack) > 0 and top_list[i] >= top_list[stack[-1]]:
        top_num = i + 1
        result[stack.pop()] = top_num
    stack.append(i)

for top in result:
    print(top, end=" ")