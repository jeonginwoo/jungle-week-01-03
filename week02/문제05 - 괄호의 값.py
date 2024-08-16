"""
출처 : 백준
번호 : 2504
난이도 : 골드 5
제목 : 괄호의 값
"""

import sys

input = sys.stdin.readline

string = input().strip()
stack = []
cal = 0
step = 1
for i in range(len(string)):
    if string[i] == '(' or string[i] == '[':
        stack.append(string[i])
        step = step * 2 if string[i] == '(' else step * 3
        if i+1 < len(string) and (string[i + 1] == ')' or string[i + 1] == ']'):
            cal += step
    elif string[i] == ')':
        if len(stack) == 0 or stack[-1] != '(':
            cal = 0
            break
        stack.pop()
        step = step / 2
    elif string[i] == ']':
        if len(stack) == 0 or stack[-1] != '[':
            cal = 0
            break
        stack.pop()
        step = step / 3
if len(stack) == 0:
    print(int(cal))
else:
    print(0)
