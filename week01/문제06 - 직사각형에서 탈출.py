"""
출처 : 백준
번호 : 1085
난이도 : 브론즈 3
제목 : 직사각형에서 탈출
"""

x, y, w, h = [int(x) for x in input().split()]
print(min(x, y, w-x, h-y))