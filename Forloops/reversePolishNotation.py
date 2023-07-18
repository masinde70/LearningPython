


def reversePlishNotation(tokens):
    """
    Time: O(n) | Space: O(n)
    where n is the number of tokens
    """
    stack = [] # Empty stack approach
    # Observe that all operations in the dictionary below are binary
    # {"operation": lambda functional operation}

    operations = {"+" : lambda a,b: a + b,
                  "-" : lambda a,b: a - b,
                  "*" : lambda a,b: a * b,
                  "/" : lambda a,b: int(a/b)}
    for token in tokens:
        if token not in operations:
            stack.append(int(token)) # Append as number
        else:
            # once we are here, we know we face an operation, 
            # thus we perform c = operation(a,b), e.g. c =  a + b
            b = stack.pop() 
            a = stack.pop()
            c = operations[token](a,b)
            stack.append(c)

    return stack[-1]

    

