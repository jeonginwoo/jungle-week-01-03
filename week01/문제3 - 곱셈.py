"""
출처 : 백준
번호 : 2588
난이도 : 브론즈 3
제목 : 곱셈
"""

a = int(input())
b = int(input())
temp = b
for i in range(3):
    num = a * (temp % 10)
    print(num)
    temp = temp // 10

print(a*b)