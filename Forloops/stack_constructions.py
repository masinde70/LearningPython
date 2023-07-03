import collections

class MinMaxStack:
    def __init__(self):
        self.maxes = []
        self.minies = []
        self.storages = []

    def peek(self):
        return self.storages[-1] if self.storages else None
    
    def pop(self):
        if self.storages:
            self.maxes.pop()
            self.minies.pop()
            return self.storages.pop()
        return None
    
    def push(self, value):
        if self.storages:
            self.maxes.append(value if value > self.maxes[-1] else self.maxes[-1])
            self.minies.append(value if value < self.minies[-1] else self.minies[-1])
        else:
            self.maxes.append(value)
            self.minies.append(value)
        self.storages.append(value)

    def getMin(self):
        if self.storages:
            