import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(3)]

num = 0

for i in range(3):
    if arr[i].isdigit():
        num = int(arr[i]) + (3 - i)

n = num

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)