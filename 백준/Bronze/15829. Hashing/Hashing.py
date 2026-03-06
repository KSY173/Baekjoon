import sys
input = sys.stdin.readline

L = int(input())
S = list(input())
r = 31
M = 1234567891
total = 0

for i in range(L):
    num = ord(S[i]) - ord('a') + 1
    a = num * (r ** i)
    total += a

H = total % M
print(H)