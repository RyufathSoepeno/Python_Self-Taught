#Try and Except statements


#They are for errors
#General coding errors ; compile time(syntax), logical, and run time error

#Statement errors are called 'Syntax Errors'
#examples ; missing ':'. wrong spellings

#Logical errors are like : wrong outputs

#Run time error : divide by zero, user/customer errors, input errors
#You need to know all the possibilities the user will do to solve run time errors

a = 5
b = 2

print(a/b)

#A line that is coded is called a statement in coding
#Types of statement, Normal and Critical
#Normal : Won't give you errors

#To avoid errors, we need to use these statements :
#Try is a critical statement, we don't know if it will work or not

a = 5
b = 0

try :
   print (a/b)
except Exception as e:
    print("You cannot divide any number by zero")

#When all fails, we "Except" the errors with "Exception" (E is upper cased)
