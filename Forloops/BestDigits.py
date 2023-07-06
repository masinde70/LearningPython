"""
Best Digits 
Write the function that takes a positive integer represented as a string number
and an integer numDigits. Remove numDigts from the string sot the number represented by the string is large as possible afterwards.

Note that the order of the remaining digits can not be changed. You can assume
numDigitswill always be be less than the length of number and greater than or equal to 0
1. We start by initializing an empty stack.
2. We traverse the string from left to right. For each digit encountered, we compare it with the top element of the stack.If the current digit is greater than the top element, we pop elements from the stack until either the stack is empty or we have popped the desired number of digits.
This step ensures that we maintain the desired order of digits in the resulting array.

3. After the traversal, we check if the entire number was in descending order. If any elements remain in the stack, we continue popping elements until we have the desired number of digits.This step handles the scenario where the input string consists of a descending sequence of digits.

4. Finally, we join the remaining elements of the stack and return the resulting array of numbers.
"""

def bestDigits(number, numDigts):
    stack = []

    for digit in number:
        while numDigts > 0 and len(stack) and digit > stack[-1]:
            stack.pop()