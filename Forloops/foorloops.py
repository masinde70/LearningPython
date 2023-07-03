# lst = [[1,2], [3,4],[5,6]]

# for i in range(len(lst)):
#     interior = lst[i]

#     for j in range(len(interior)):
#         print(interior[j])

# st = "hello world"

# for i, char in enumerate(st):
#     if char == 'w':
#         print(i)

numbers = []
for i in range(10):
    num = input("Enter a number: ")
    numbers.append(num)

print(numbers)
# use a single loop to iterate through the list and print that are both divisble by 2 and located at an odd index, each on separate lines line
lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

# Write your code here.
for i in range(len(lst)):
    item = lst[i]

    if item % 2 == 0 and i % 2 != 0:
        print(item)


