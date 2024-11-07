class Person:
    name = "Mike"
    age = 33
    high = 185

print(Person.name, Person.age)

Person.age = 50
print(Person.name, Person.age)

print(Person.__dict__)

person01 = Person()
person02 = Person()

print(f"person01: {person01}")
print(f"person02: {person02}")

print(f"person01: {person01.name}, {person01.age}, {person01.high}")
print(f"person02: {person02.name}, {person02.age}, {person01.high}")

person01.hobby = "chess"
print(f"person01: {person01.__dict__}")
print(f"person02: {person02.__dict__}")
print(f"Person: {Person.__dict__}")