class Queue:
    def __init__(self, limit):
        self.limit = limit
        self.items = [None] * limit
        self.start = -1
        self.end = -1
        self.current_size = 0
    
    def is_size_full(self) -> bool:
        if self.current_size == self.limit:
            return True
        return False

    
    def push(self, item) -> None:
        if not self.is_size_full():
            if self.start == -1:
                self.start += 1
            self.end = (self.end + 1) % self.limit
            self.current_size += 1
            self.items[self.end] = item
        else:
            print("queue is full")
    
    def pop(self):
        if self.current_size == 0:
            print("pop operation cannot be performed, the qeueu is already empty")
            return
        ele = self.items[self.start]
        if self.current_size == 1:
            self.start , self.end = -1, -1
        else:
            self.start = (self.start + 1) % self.limit
        
        self.current_size -= 1
        
        print(ele)

    def top(self):
        if self.current_size == 0:
            print("the queue is empty")
            return
        print(self.items[self.start])
    
    def __str__(self):
        return str(self.items)

obj = Queue(2)
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
obj.pop()
obj.pop()
obj.push(4)
obj.push(5)
obj.top()
obj.pop()

print(obj)