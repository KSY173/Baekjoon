import sys
input = sys.stdin.readline

T = int(input().strip())

A = [[0] * 15 for _ in range(15)]

for n in range(1, 15):
    A[0][n] = n

for k in range(1, 15):
    for n in range(1, 15):
        A[k][n] = A[k][n-1] + A[k-1][n]

for _ in range(T):
    k = int(input().strip())
    n = int(input().strip())
    print(A[k][n])