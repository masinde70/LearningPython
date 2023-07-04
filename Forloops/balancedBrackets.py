def balancedBrackets(string):
    openBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "[" :"]", "}":"{"}
    stack = []

    for char in string:
        if char in openBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

