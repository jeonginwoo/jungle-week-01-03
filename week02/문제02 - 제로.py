"""
출처 : 백준
번호 : 10773
난이도 : 실버 4
제목 : 제로
"""

import sys
input = sys.stdin.readline
K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))