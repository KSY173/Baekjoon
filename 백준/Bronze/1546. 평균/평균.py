import sys
input = sys.stdin.readline
N = int(input())
scores = list(map(int, input().split()))

max_sc = max(scores)
new_scores = [(s / max_sc) * 100 for s in scores]

print(sum(new_scores) / N)