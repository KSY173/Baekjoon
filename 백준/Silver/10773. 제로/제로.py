import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def total_sum(self):
        current = self.top
        result = 0
        while current:
            result += current.data
            current = current.next
        return result

K = int(input())
stack = Stack()

for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.push(num)

print(stack.total_sum())