"""
출처 : 백준
번호 : 11279
난이도 : 실버 2
제목 : 최대 힙
"""

import sys
input = sys.stdin.readline

def heapPush(L, val):
    k = len(L)
    L.append(val)
    while k > 0:
        p = (k-1) >> 1
        if L[p] < L[k]:
            L[p], L[k] = L[k], L[p]
        k = p

def heapPop(L):
    if len(L) == 0:
        return 0
    L[0], L[-1] = L[-1], L[0]
    max_num = L.pop()
    k = 0
    temp_k = (k >> 1) + 1
    while temp_k < len(L):
        c1 = temp_k
        c2 = temp_k + 1
        if c2 < len(L):
            if L[c1] > L[c2]:
                if L[c1] > L[k]:
                    L[c1], L[k] = L[k], L[c1]
                    k = c1
            else:
                if L[c2] > L[k]:
                    L[c2], L[k] = L[k], L[c2]
                    k = c2
        else:
            if L[c1] > L[k]:
                L[c1], L[k] = L[k], L[c1]
                k = c1
        temp_k = (k >> 1) + 1

    return max_num


N = int(input())
max_heap = []
for _ in range(N):
    num = int(input())
    if num == 0:
        print(heapPop(max_heap))
    else:
        heapPush(max_heap, num)
