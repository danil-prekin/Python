class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def pop(self):
        if self.start is None:
            raise IndexError("Очередь пуста")
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def insert(self, n, val):
        if n < 0:
            raise ValueError("Некорректная позиция")
        current = self.start
        for _ in range(n-1):
            if current is None:
                raise IndexError("Позиция вне диапазона")
            current = current.nref
        new_node = Node(val)
        if current is None:
            self.push(val)
        else:
            next_node = current.nref
            new_node.pref = current
            new_node.nref = next_node
            current.nref = new_node
            if next_node:
                next_node.pref = new_node
            else:
                self.end = new_node

    def print(self):
        current = self.start
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.nref
        print(" ".join(elements)) if elements else print("Очередь пуста")