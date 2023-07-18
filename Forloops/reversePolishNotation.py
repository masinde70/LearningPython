


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
    

