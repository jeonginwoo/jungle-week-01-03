"""
출처 : 백준
번호 : 11866
난이도 : 실버 4
제목 : 요세푸스 문제 0
"""

from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
people = deque()
for person in range(1, N + 1):
    people.append(person)

yo = []
while len(people) > 0:
    people.rotate(-K + 1)
    yo.append(people.popleft())

print(f"<{', '.join(map(str, yo))}>")