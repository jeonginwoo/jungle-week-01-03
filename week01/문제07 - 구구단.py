"""
출처 : 백준
번호 : 2739
난이도 : 브론즈 5
제목 : 구구단
"""

N = int(input())
for i in range(1, 10):
    print('{0} * {1} = {2}'.format(N, i, N*i))