"""
Next Greater Element 
Write a function that takes in array of integers and returns
a new array containing at each index the next element in the
input array that is greater than the element at index in the
input array.

In other words, the function should return a new array where
outputArray[i] is the next element in the input array that is greater
than inputArray[i]. If there's no such next greater element for particular index,
the value at that particular index in the output array should be
-1. For example, given array = [1, 2], your function should
return [2, -1].

Additionally, the function should treat the input array as 
circular array. A circular array wraps around itself as if it
were connected end to end. So the next index after the last index in circular array is the
first index. This means that, for our problem, 
given array = [0, 0, 5, 0,0,3,0,0] the next element after 3 is 5
since the array is circular array.

"""

#O(n) time | O(n) space - where n is the length of the array
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for index in range(2 * len(array)):
        circularIndex = index % len(array)

        while len(stack) > 0 and array[stack[len(stack) - 1]] < array[circularIndex]:
            top = stack.pop()
            result[top] = array[circularIndex]
        stack.append(circularIndex)
    return result