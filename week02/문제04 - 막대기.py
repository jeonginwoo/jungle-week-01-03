"""
출처 : 백준
번호 : 17608
난이도 : 브론즈 2
제목 : 막대기
"""

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    next_stick = int(input())
    while len(stack) > 0 and stack[-1] <= next_stick:
        stack.pop()
    stack.append(next_stick)
print(len(stack))