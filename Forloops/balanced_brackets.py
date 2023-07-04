def balanced_brackets(string):
    pairs = {'(':')', '[':']', '{':'}'}
    stack = []

    for x in string:
        if x not in '([{}])':
            continue
        elif not stack or pairs.get(stack[-1]) != x:
            stack.append(x)
        else:
            stack.pop()
    return len(stack) == 0
