import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

count_dict = {}

for num in cards:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for num in targets:
    if num in count_dict:
        print(count_dict[num], end=' ')
    else:
        print(0, end=' ')