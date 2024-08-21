import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, sys.stdin.read().split())) + [float("inf")]
stack = [0]
count = [0] * N

for i in range(1, N + 1):
    while stack and H[stack[-1]] <= H[i]:
        idx = stack.pop()
        count[idx] = i - idx - 1
    stack.append(i)
print(sum(count))
