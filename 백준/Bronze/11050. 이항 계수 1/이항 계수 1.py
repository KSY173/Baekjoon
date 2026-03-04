import sys
input = sys.stdin.readline
import math

n, k = map(int, input().split())
a = math.factorial(n-k)
b = math.factorial(k)
c = math.factorial(n)

print(c//(a*b))