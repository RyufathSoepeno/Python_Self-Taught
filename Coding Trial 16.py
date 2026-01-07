#Further explanations of Arguments 


#def_function name_(the variable to pass)

def update (x):
    x = 8
    print(x)


a = 10
update(a)
print(update)
print(a)

# Define Arguments = Pass
# print(a) = Pass by Value
# print (update) = Pass by Reference



#Types of Argument


#The first Argument in "this" program,
#(x) = Formal Argument
# print (x), or update(a) = Actual Argument


#Keyboard Argument (Usually caused by algorithm errors)

def person(name, age):
    print(name)
    print(age)

#The simple and correct way

person("Ryu", 17)

#Keyboard Argument way

person(age = 17, name = "Ryu")




    
