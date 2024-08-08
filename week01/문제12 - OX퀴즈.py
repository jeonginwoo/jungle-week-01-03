"""
출처 : 백준
번호 : 8958
난이도 : 브론즈 2
제목 : OX퀴즈
"""

N = int(input())
for i in range(N):
    quiz = input()
    point = 1
    sum = 0
    for answer in quiz:
        if answer == 'O':
            sum += point
            point += 1
        else:
            point = 1
    print(sum)
