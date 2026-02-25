import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ans = 0

for x in nums:
    if x == 1:          
        continue

    count = 0

    for d in range(1, x + 1):
        if x % d == 0:
            count += 1

    if count == 2:
        ans += 1

print(ans)