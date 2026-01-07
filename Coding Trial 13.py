#Telusko's Explanations for Functions


#Greet is a named function

#The reason to put () is to tell that it is a function, not a variable

def greet ():
    print("Hello")
    print("Good Morning")

#Print reveals a a variable
#Or in some cases, things with '='
#To that, functions are one of the things where you don't use print


greet()

def add(x, y):
    c = x+y
    print(c)

add(5, 4)

#Using 'return'

def add(x, y):
    c = x+y
    return c

result = add(5, 4)
print(result)


