import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  R, S = input().split()
  R = int(R)

  result = ''.join(ch * R for ch in S)

  print(result)