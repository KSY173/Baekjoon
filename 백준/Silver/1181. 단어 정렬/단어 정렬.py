import sys
input = sys.stdin.readline

N = int(input())
words = set()
for i in range(N):
    s = input().strip()
    words.add(s)

sorted_words = sorted(words, key=lambda x: (len(x), x))

for w in sorted_words:
    print(w)