"""
출처 : 백준
번호 : 1541
난이도 : 실버 2
제목 : 잃어버린 괄호
"""


cal = [list(map(int, item.split("+"))) for item in input().split("-")]

result = sum(cal[0])
sub = 0
for i in range(1, len(cal)):
    sub += sum(cal[i])
result -= sub
print(result)