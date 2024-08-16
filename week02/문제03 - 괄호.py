"""
출처 : 백준
번호 : 9012
난이도 : 실버 4
제목 : 괄호
"""

import sys
input = sys.stdin.readline


def isVPS(str):
    stack = []
    for i in range(len(str)-1):
        if str[i] == "(":
            stack.append(str[i])
        elif str[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())

for _ in range(T):
    print("YES" if isVPS(input()) else "NO")
