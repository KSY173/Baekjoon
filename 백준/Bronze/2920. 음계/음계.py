import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
count = 0
for i in range(8):
    if arr[i] == i + 1 :
        count += 1
    elif arr[i] == 8 - i:
        count -= 1
if count == 8:
    print("ascending")
elif count == -8:
    print("descending")
else:
    print("mixed")