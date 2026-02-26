import sys
input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

print(A + B - C)

AB_str = str(A) + str(B)
AB_num = int(AB_str)
print(AB_num - C)