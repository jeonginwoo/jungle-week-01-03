"""
출처 : 백준
번호 : 2812
난이도 : 골드 3
제목 : 크게 만들기
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()
num_split = [int(s) for s in num[::-1]]
num_save = []

count = 0
while num_split:
    while num_save and count < K and num_save[-1] < num_split[-1]:
        num_save.pop()
        count += 1
    num_save.append(num_split.pop())
for i in range(K-count):
    num_save.pop()
print(*num_save,sep='')