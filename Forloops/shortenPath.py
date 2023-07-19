class Stack:
    def __init__(self):
        self.stack = list()

    def pop(self):
        if self.empty() is False:
            return self.stack.pop()
    
    def push(self, value):
        self.stack.append(value)

    def empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def __str__(self) -> str:
        return str(self.stack)
    