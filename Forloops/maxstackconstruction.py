class MinMaxStack:
    def __init__(self):
       self.minMaxStack = []
       self.stack = []
    #O(1) time | O(1) space 
    def peek(self):
        return self.stack[len(self.stack)-1]
    