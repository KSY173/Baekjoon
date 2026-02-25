import sys
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None    

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def peek(self):
        if self.is_empty():
            return -1
        return self.top.data

    def pop(self):
        if self.is_empty():
            return -1
        current = self.top
        self.top = self.top.next
        self._size -= 1
        return current.data
    
    def size(self):
        return self._size
    
    def empty(self):
        return 1 if self.is_empty() else 0
    
N = int(input())
stack = Stack()
out = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        stack.push(int(cmd[1]))
    elif cmd[0] == "pop":
        out.append(str(stack.pop()))
    elif cmd[0] == "size":
        out.append(str(stack.size()))
    elif cmd[0] == "empty":
        out.append(str(stack.empty()))
    elif cmd[0] == "top":
        out.append(str(stack.peek()))

print("\n".join(out))
