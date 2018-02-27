class Person():
    species = 'Human'

print(Person.species) #Human
Person.alive = True #added dynamically
print(Person.alive) #True

man = Person
print(man.species) #Human Inherited
print(man.alive) #True (inherited)

Person.alive = False
print(man.alive) #False(Inherited)

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)
"""
In this example, there is a class attribute called species. Any variable defined in the body of a class is an atribute
that belongs to that class.
There is another atribute called alive.This shows there is no restriction on accessing that attribute from the class
Man which is an instance of Person, inherits both of them, and reflects them instantly when they change

Man also has two attributes which belong to its own namespace and therefore are called instace atributes: name and surname

NOTE Class attributes are shared among all instances, while instance attributes are not; therefore, you should use class attributes to provide the states
and behaviors to be shared by all instances, and use instance attributes for data that belongs to just one specific object.
"""