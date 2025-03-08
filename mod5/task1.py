class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def pop(self):
        if self.end is None:
            raise IndexError("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def print(self):
        current = self.end
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.pref

        print(" ".join(reversed(elements)) if elements else "Стек пуст")