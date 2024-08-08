"""
출처 : 백준
번호 : 2675
난이도 : 브론즈 2
제목 : 문자열 반복
"""

T = int(input())
for i in range(T):
    R, S = [x for x in input().split()]
    string = ""
    for j in S:
        string += j * int(R)
    print(string)
