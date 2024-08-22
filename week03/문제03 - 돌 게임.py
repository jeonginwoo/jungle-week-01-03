"""
출처 : 백준
번호 : 1904
난이도 : 실버 5
제목 : 돌 게임
"""

import sys
input = sys.stdin.readline


N = int(input())
count = N // 3 + N % 3
if count % 2 == 0:
    print("CY")
else:
    print("SK")