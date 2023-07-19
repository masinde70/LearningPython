class Stack:
    def __init__(self):
        self.stack = list()

    def pop(self):
        if self.empty() is False:
            return self.stack.pop()