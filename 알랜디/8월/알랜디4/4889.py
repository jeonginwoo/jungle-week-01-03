import sys
input = sys.stdin.readline


def function(string):
    stack = []
    count = 0
    for i in range(len(string)):
        now = string[i]
        if now == "{":
            stack.append(now)
        elif now == "}":
            if not stack:
                count += 1
                stack.append("{")
                continue
            stack.pop()
    count += len(stack) // 2
    return count


step = 1
while True:
    string = input().strip()
    if string[0] == "-":
        break

    print(f"{step}. {function(string)}")
    step += 1
