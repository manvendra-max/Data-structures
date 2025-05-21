class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("Cannot perform pop operation, the stack is empty")
            return
        temp = self.top
        self.top = self.top.next
        data = temp.data
        del temp
        self.size -= 1
        return data

    
    def print_top(self):
        return self.top.data if self.top else None  
    
    def show_size(self):
        return self.size


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)

print(stack.pop())
stack.pop()
stack.push(45)
stack.pop()
print(stack.print_top())
print(stack.show_size())

