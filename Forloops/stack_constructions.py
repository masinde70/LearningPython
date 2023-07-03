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
    