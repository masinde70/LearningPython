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
    
    def __str__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)
    
    def top(self):
        if self.empty() is False:
            return self.stack[-1]
        
    def return_as_list(self):
        return self.stack

def shortenPath(path):
    stack = Stack()
    absolute = False

    if path[0] == '/': absolute = True

    directories = path.split('/')

    for dir in directories:
        if dir == '.' or dir == '':
            continue
            
        elif dir == '..':
            if stack.empty() and not absolute:
                stack.push(dir)
            elif absolute or stack.top() != '..':
                stack.pop()
            else:
                stack.push(dir)
        else:
            stack.push(dir)
    result = '/'.join(stack.return_as_list())

    if absolute is True: return '/' + result

    return result