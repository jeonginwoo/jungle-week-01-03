"""
출처 : 백준
번호 : 2869
난이도 : 브론즈 1
제목 : 달팽이는 올라가고 싶다
"""

import math

A, B, V = [int(x) for x in input().split()]
print(math.ceil((V-A)/(A-B))+1)
