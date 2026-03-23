import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

# 1. 산술평균
avg = round(sum(nums) / N)

# 2. 중앙값
median = nums[N // 2]

# 3. 최빈값
count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1

max_freq = max(count.values())
modes = []

for num in count:
    if count[num] == max_freq:
        modes.append(num)

modes.sort()

if len(modes) == 1:
    mode = modes[0]
else:
    mode = modes[1]

# 4. 범위
range_value = nums[-1] - nums[0]

print(avg)
print(median)
print(mode)
print(range_value)