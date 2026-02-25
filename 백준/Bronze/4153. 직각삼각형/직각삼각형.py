import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    # 0 0 0이면 입력 종료
    if a == 0 and b == 0 and c == 0:
        break

    sides = sorted([a, b, c])  # 오름차순 정렬

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")