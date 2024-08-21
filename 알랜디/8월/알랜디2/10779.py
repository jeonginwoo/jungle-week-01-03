import sys
input = sys.stdin.readline

string = input().strip()

result = 0
stack = []
for s in range(len(string)):
    if string[s] == '(':
        stack.append(string[s])
    elif string[s] == ')':
        stack.pop()
        if string[s-1] == '(':
            result += len(stack)
        elif string[s-1] == ')':
            result += 1
print(result)