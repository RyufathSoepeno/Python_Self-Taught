#Classes 

#We can use classes to define new types to model new concepts

#Class is the blueprint, Object is the building
#Objects is an instance of a class, a class is a template

#Instead of just using list only, and other python terms;
#We can use classes

#Use Pascal naming for class ; class_Class Name
#Always capitalize the class' first letter
#if it has two words, do this --> Ex : ClientEmail

class User:
    pass

user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name, user1.last_name)

#To type out the name of the class, call it lke a 'Function'
#Reminder = Functions can also act like buttons


#"pass" is already a class method itself
# 'user1" is called an "Instance Object" of the class

#Object.Variable_Name
#Exercise caution for classes because they can cause attribute error
#Because they can't read other versions of the class methods






