"""
출처 : 백준
번호 : 5568
난이도 : 실버 4
제목 : 카드 놓기
"""


def unionCard(k, cards, union, s):
    if k < 1:
        s.add(union)
        return
    for i in range(len(cards)):
        tempCards = cards[:]
        del tempCards[i]
        unionCard(k - 1, tempCards, union + cards[i], s)


n = int(input())
k = int(input())

cards = []
for _ in range(n):
    cards.append(input())

s = set({})
union = ""
unionCard(k, cards, union, s)

print(len(s))
