"""
출처 : 백준
번호 : 9498
난이도 : 브론즈 5
제목 : 시험 성적
"""

point = int(input())

if 90 <= point <= 100:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("F")
