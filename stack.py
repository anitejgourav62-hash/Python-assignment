class Stack:
    def __init__(self):
        self.stack = []  

    # Method to push element into stack
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    # Method to safely pop element
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()

    # Method to display stack
    def display(self):
        print("Stack:", self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())

# Trying to pop from empty stack
print("Popped:", s.safe_pop())