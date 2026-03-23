import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

answer = 64  # 8x8 최대 다시 칠하는 수

for x in range(N - 7):
    for y in range(M - 7):
        repaint_w = 0  # 왼쪽 위가 W인 경우
        repaint_b = 0  # 왼쪽 위가 B인 경우

        for i in range(8):
            for j in range(8):
                current = board[x + i][y + j]

                # (i+j)가 짝수면 시작색과 같아야 함
                if (i + j) % 2 == 0:
                    if current != 'W':
                        repaint_w += 1
                    if current != 'B':
                        repaint_b += 1
                else:
                    if current != 'B':
                        repaint_w += 1
                    if current != 'W':
                        repaint_b += 1

        answer = min(answer, repaint_w, repaint_b)

print(answer)