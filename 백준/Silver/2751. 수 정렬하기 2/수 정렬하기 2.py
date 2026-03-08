import sys
input = sys.stdin.readline

N = int(input().strip())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)