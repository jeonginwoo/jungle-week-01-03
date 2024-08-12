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

def set(col):
    global N, checkRow, checkLineA, checkLineB, count
    for row in range(N):
        if (not checkRow[row]
                and not checkLineA[col - row + N - 1]
                and not checkLineB[col + row]):
            # pos[col] = row
            if col == N - 1:
                count += 1
                # put()
            else:
                checkRow[row] = checkLineA[col - row + N - 1] = checkLineB[col + row] = True
                set(col + 1)
                checkRow[row] = checkLineA[col - row + N - 1] = checkLineB[col + row] = False


N = int(input())

# pos = [0] * N
checkRow = [False] * N
checkLineA = [False] * (2 * N - 1)  # 대각선 a
checkLineB = [False] * (2 * N - 1)  # 대각선 b
count = 0

set(col=0)
print(count)
