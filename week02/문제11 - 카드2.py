"""
출처 : 백준
번호 : 2164
난이도 : 실버 4
제목 : 카드2
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cards = deque()
for card in range(1, N + 1):
    cards.append(card)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])