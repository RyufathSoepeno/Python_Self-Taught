#Complex try statements

#Pretend it is like taking an object from a fridge
#You make sure you closed it, even if there are Exception
#Exception examples : Someone called youy to go to him/her

#Which means, when you opene the resource, always close it

a = 5
b = 0

try :
    print("Opening the file")
    print(a/b)
except Exception as e:
    print("IT IS RAW !!!!!")

finally:
    print("Closing the file")

#Finally means, you are getting the output, even if there is an error or not

#If there were no errors
    
a = 5
b = 2

try :
    print("Opening the file")
    print(a/b)
except Exception as e:
    print("IT IS RAW !!!!!")

finally:
    print("Closing the file")

#using inputs

try:
    k = int(input("Enter a number"))
    print (k)
except Exception as e:
    print("Enter a number, not a word")

#Creating exceptions of zero error

a = 6
b = 0

try:
    print("Opening the file")
    print(a/b)
except ZeroDivisionError as f:
    print("It is undefined")

#Except_Exceptions/Errors_As_Naming the statement
