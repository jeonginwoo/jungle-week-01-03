"""
출처 : 백준
번호 : 2110
난이도 : 골드 4
제목 : 공유기 설치
"""

import sys

N, C = map(int, input().split())
listX = sorted([int(x) for x in sys.stdin.read().split()])
start = 1
end = listX[-1] - listX[0]
result = 0
while start <= end:
    mid = (start + end) // 2

    count = 1
    dist = 0
    now = listX[0]
    for i in range(1, N):
        dist = listX[i] - now
        if dist >= mid:
            dist = 0
            now = listX[i]
            count += 1
    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)