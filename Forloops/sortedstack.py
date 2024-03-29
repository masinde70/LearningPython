"""Write a function that takes in an array of integers representing a stack, recursively sorts the stack in place
  (i.e doesn't create new array), and returns it.
  The array must be treated as stack, with the end of the array as the top of the stack. Therefore, you are only allowed
  to
  1. Pop elements from the stack by removing elements to the end of the array using the built-in .pop()
  2. Push elements to the top of the stack by appending elements to the end of the array using the built-in .append()
  3. Peek at the element on the top of the stack by accessing the last element in the array.
 """


def sortedStack(stack):
    if len(stack) <= 1:
        return stack
    
    v1 = stack.pop()
    sortedStack(stack)
    v2 = stack.pop()

    if v2 > v1:
        stack.append(v1)
        sortedStack(stack)
        stack.append(v2)
    else:
        stack.append(v2)
        stack.append(v1)

    return stack


    