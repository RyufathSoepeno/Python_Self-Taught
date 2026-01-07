#Input and User Input


#It is used to fill in our own numbers
#Very resourceful for client use

x = input("Enter 1st number")
y = input("Enter 2nd number")
z = x + y
print(z)

#The shell (Console) is waiting for input from user
#User doesn't know what to do

#Type something beside the input string to run code fully


#To make in an addition
#You need to change it to variable format, not string format
#Int is integer
#Int returns an integer from a variable/number or string when an argument is given

x = input("Enter 1st number")
a = int(x)
y = input("Enter 2nd number")
b = int(y)
z = a + b
print(z)

#Or for short

x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))
z = x + y
print(z)


#How to make using character format

ch = len(input("Enter your word"))

print(ch)

#Spaces will be counted

dhx = input("Enter your word")

print(dhx[1])

#Or for short again

dhx = input("Enter your word")[1]

print(dhx)
    

#How to use expression formats. (Input[x + y = z])
#Use eval. Eval passes data to user
#Do not input words or symbols

camp = eval(input("Enter an expression"))
print(camp)

result = eval

