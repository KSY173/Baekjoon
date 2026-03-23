import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque((i, priorities[i]) for i in range(N))
    order = 0

    while queue:
        idx, priority = queue.popleft()

        if any(priority < q_priority for _, q_priority in queue):
            queue.append((idx, priority))
        else:
            order += 1
            if idx == M:
                print(order)
                break