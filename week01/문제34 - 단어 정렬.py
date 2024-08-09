"""
출처 : 백준
번호 : 1181
난이도 : 실버 5
제목 : 단어 정렬
"""

N = int(input())
wordList = set()
for _ in range(N):
    wordList.add(input())
wordList = list(wordList)

wordList.sort(key=lambda x: (len(x), x))
for word in wordList:
    print(word)
