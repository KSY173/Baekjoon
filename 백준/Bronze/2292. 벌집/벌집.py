import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    layer = 1      
    end = 1

    while N > end:
        end += 6 * layer 
        layer += 1

    print(layer)