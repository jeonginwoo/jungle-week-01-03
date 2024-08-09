"""
출처 : 백준
번호 : 2628
난이도 : 실버 5
제목 : 종이자르기
"""

width, height = [int(x) for x in input().split()]
N = int(input())
col = [0]
row = [0]
for _ in range(N):
    select, idx = [int(x) for x in input().split()]
    if select == 0:
        row.append(idx)
    else:
        col.append(idx)
col.sort()
row.sort()
col.append(width)
row.append(height)
area = []

for c in range(1, len(col)):
    for r in range(1, len(row)):
        area.append((col[c] - col[c - 1]) * (row[r] - row[r - 1]))
print(max(area))