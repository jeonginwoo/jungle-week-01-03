"""
출처 : 백준
번호 : 10871
난이도 : 브론즈 5
제목 : X보다 작은 수
"""

N, X = [int(x) for x in input().split()]
for i in [int(x) for x in input().split()]:
    if i < X:
        print(i, end=" ")