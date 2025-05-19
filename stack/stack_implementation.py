class Stack:
    def __init__(self, limit: int):
         self.limit = limit
         self.items = []
         self.top = -1

    
    def show_top(self) -> None:
         '''this will print top of stack'''
         print(self.items[self.top])
    
    def push(self, item: int) -> None:
         if (self.top + 1 >= self.limit):
              print("the stack is full")
              return
         
         self.items.append(item)
         self.top += 1
         print(f'{item} has been pushed to the stack')
    
    def pop(self) -> None:
         if self.top <= 0:
              print("the stack is empty")
              return 
         self.items.pop(self.top)
         self.top -= 1
    
    def __str__(self):
         return str(self.items)

obj = Stack(4)
obj.push(1)
obj.push(2)
obj.pop()
obj.pop()
obj.pop()
obj.push(4)
obj.push(5)
obj.push(0)
obj.push(6)
print(obj)