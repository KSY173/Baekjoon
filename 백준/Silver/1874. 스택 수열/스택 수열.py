import sys
input = sys.stdin.readline

n = int(input())
targets = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for target in targets:
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1

    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    print('\n'.join(result))