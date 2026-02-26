import sys
input = sys.stdin.readline

N = int(input())

start = max(1, N - 9 * len(str(N)))

result = 0

for M in range(start, N):
    if M + sum(map(int, str(M))) == N:
        result = M
        break

print(result)