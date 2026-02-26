import sys
input = sys.stdin.readline

N = int(input())
nums = input().strip()

total = sum(int(x) for x in nums)
print(total)