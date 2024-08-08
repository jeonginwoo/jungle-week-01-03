"""
출처 : 백준
번호 : 2588
난이도 : 브론즈 3
제목 : 시험 성적
"""

point = int(input())

if point >= 90 and point <= 100:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("E")
