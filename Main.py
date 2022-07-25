import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top=-1

    def is_empty(self):
        return self.top==-1
       
        

    def is_full(self):
        return self.top==s.n-1

    def push(self, data):
        if not self.is_full():
            print("STACK IS FULL")
        else:
            s.top+=1
            x=int(input("Enter data : "))
            s.st[s.top]=x

    def pop(self):
        if not self.is_empty():
            if(self.top == -1): 
            print("Stack is full") 
            print("Underflow condition is occured ") 
            print("\n") 
        else:             
            self.top -= 1 
            self.Array.pop()
            

    def status(self):
       for i in range (s.top+1):
            print(s.st[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
