arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

max = arr[0]
max_index = 0
for i in range(9):
    if arr[i] >= max:
        max = arr[i]
        max_index = i + 1
        
print(max)
print(max_index)