"""
출처 : 백준
번호 : 2110
난이도 : 골드 4
제목 : 공유기 설치
"""

import sys

N, C = map(int, input().split())
X = sorted(int(line) for line in sys.stdin.read().split())
result = 0

start = 1
end = X[-1] - X[0]
while start <= end:
    mid = (start + end) // 2
    count = 1
    now = X[0]
    for i in range(1, N):
        if X[i] - now >= mid:
            now = X[i]
            count += 1
    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)