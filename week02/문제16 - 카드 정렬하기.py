"""
출처 : 백준
번호 : 1715
난이도 : 골드 4
제목 : 카드 정렬하기
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
deck = list(map(int, sys.stdin.read().split()))
heapq.heapify(deck)

min_sum = 0
while len(deck) > 1:
    A = heapq.heappop(deck)
    B = heapq.heappop(deck)
    C = A + B
    min_sum += C
    heapq.heappush(deck, C)

print(min_sum)