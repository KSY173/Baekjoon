import sys
input = sys.stdin.readline

N = int(input())
x = []
y = []
sc = []

for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

count = 0

for i in range(N):
    for j in range(N):
        if x[i] < x[j] and y[i] < y[j]:
            count += 1
    sc.append(count + 1)
    count = 0

for i in range(N):
    print(sc[i], end=" ")