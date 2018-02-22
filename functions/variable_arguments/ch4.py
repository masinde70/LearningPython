people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium','Spain','England','Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, 'Age', age, nationality)

n = 39
remainders = []
while n > 0:
    remainder = n %2 #Remainder of division by 2
    remainders.append(remainder) # we keep track of remainders
    n //= 2 # We divide by 2

#Reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)