"""
출처 : 백준
번호 : 2753
난이도 : 브론즈 5
제목 : 윤년
"""

year = int(input())
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(1)
else:
    print(0)