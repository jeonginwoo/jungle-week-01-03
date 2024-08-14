"""
출처 : 백준
번호 : 9663
난이도 : 골드 4
제목 : N-Queen
"""

# def put():
#     for j in range(N):
#         for i in range(N):
#             print('●' if pos[i] == j else '○', end='  ')
#         print()
#     print()

def queen(i):
    global N, line1, line2, line3, count
    for j in range(N):
        if not line1[j] and not line2[i + j] and not line3[i - j + N - 1]:
            # pos[i] = j
            if i == N - 1:
                count += 1
                # put()
            else:
                line1[j] = line2[i + j] = line3[i - j + N - 1] = True
                queen(i+1)
                line1[j] = line2[i + j] = line3[i - j + N - 1] = False


N = int(input())
# pos = [0] * N
line1 = [False] * N
line2 = [False] * (2 * N - 1)
line3 = [False] * (2 * N - 1)
count = 0
queen(0)
print(count)
