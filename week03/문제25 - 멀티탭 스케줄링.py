"""
출처 : 백준
번호 : 1700
난이도 : 골드 1
제목 : 멀티탭 스케줄링
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use_seq = list(map(int, input().split()))

is_in = [False]*101
multitap = []
result = 0

for i in range(K):
    item = use_seq[i]
    if is_in[item]:
        continue
    if len(multitap) < N:
        multitap.append(item)
        is_in[item] = True
        continue

    pop_item_idx = 0
    max_idx = -1
    for j in range(N):
        next_seq = use_seq[i+1:]
        use_item = multitap[j]
        if use_item not in next_seq:
            pop_item_idx = j
            break
        idx = next_seq.index(use_item)
        if idx > max_idx:
            max_idx = idx
            pop_item_idx = j

    is_in[multitap[pop_item_idx]] = False
    multitap[pop_item_idx] = item
    is_in[item] = True
    result += 1

print(result)
