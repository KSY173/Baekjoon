import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def empty(self):
        return 1 if self.head is None else 0

    def pop(self):
        if self.head is None:
            self.tail = None
            return -1

        current = self.head
        self.head = current.next

        if self.head is None:
            self.tail = None

        return current.data

    def size(self):
        current = self.head
        cnt = 0
        while current:
            cnt += 1
            current = current.next
        return cnt

    def front(self):
        if self.head is None:
            return -1
        return self.head.data

    def back(self):
        if self.tail is None:
            return -1
        return self.tail.data

N = int(input())
queue = Queue()
out = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        queue.push(int(cmd[1]))
    elif cmd[0] == "pop":
        out.append(str(queue.pop()))
    elif cmd[0] == "size":
        out.append(str(queue.size()))
    elif cmd[0] == "empty":
        out.append(str(queue.empty()))
    elif cmd[0] == "front":
        out.append(str(queue.front()))
    elif cmd[0] == "back":
        out.append(str(queue.back()))

print("\n".join(out))