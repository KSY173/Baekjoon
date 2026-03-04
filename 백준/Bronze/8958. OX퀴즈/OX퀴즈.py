import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = input().strip()   
    count = 0            
    nums = []

    for s in arr:
        if s == "O":
            count += 1
            nums.append(count)
        else:
            count = 0

    print(sum(nums))