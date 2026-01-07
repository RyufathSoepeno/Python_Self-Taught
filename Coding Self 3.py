#Functions in Python


#Functions is a collection of code/instructions

#Functions can be named anything after def


#Define functions are used to provide the required functionality

#def_Function Name ()

def function1():
    print ("ahhh")
    print ("ahhh2")
print("this is outside (ahhh) functions")

#You must put function1 to start a function

function1()

#You can use functions to run a code more than once

function1()

function1()

#Functions can also mean MAPPING

#() is input or an argument

#Missing an argument after another argument will make an error

#Return is a final output value

def function2(x):
    return 2*x

#To call this function out

a = function2(3)

print (a)

#Functions with two arguments

def function3(x, y):
    return x + y

f = function3(21, 19)

print (f)

#Combining to function outputs

#This works by 

def function4(x):
    print(x)
    print("Still in this function")
    return 3*x

o = function4(12)

print (o)

def function5(some_argument):
    print(some_argument)
    print("Weeeeeeeeeee")

function5(4)

#Even if function is given an argument, we don't get a return value

#It would be pretty useless to use a variable without the return button
