#Random Import


import random

#Shouldn't be used for security and cryptography

value = random.random()
print(value)

#Just random is only in range between 0 - 1

value = random.uniform(1, 10)
print(value)

#If you don't want floats
#randint is for ramdom integers

value = random.randint(1, 10)
print(value)


#If you want strings (Since they are random and not definite like numbers)

greetings = ("hello", "Hola", "Hi", "Love from above")

value = random.choice(greetings)
print(value + " Ryu")

