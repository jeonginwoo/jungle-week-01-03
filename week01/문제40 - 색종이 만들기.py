"""
출처 : 백준
번호 : 2630
난이도 : 실버 2
제목 : 색종이 만들기
"""


def splitPaper(N, lu, rd):
    global paper, count
    cnt0 = 0
    cnt1 = 0
    for i in range(lu[0], rd[0] + 1):
        for j in range(lu[1], rd[1] + 1):
            if paper[i][j] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
    if cnt0 * cnt1 == 0:
        if cnt0 != 0:
            count[0] += 1
        else:
            count[1] += 1
        return
    cutX = (lu[0] + rd[0]) // 2
    cutY = (lu[1] + rd[1]) // 2
    splitPaper(N // 2, lu, (cutX, cutY))
    splitPaper(N // 2, (lu[0], cutY + 1), (cutX, rd[1]))
    splitPaper(N // 2, (cutX + 1, lu[1]), (rd[0], cutY))
    splitPaper(N // 2, (cutX + 1, cutY + 1), rd)


N = int(input())
paper = []
for _ in range(N):
    paper.append([int(x) for x in input().split()])

count = [0, 0]
splitPaper(N, (0, 0), (N - 1, N - 1))
print(count[0])
print(count[1])
