#Further explanations of classes


#init method = Initialization (Constructors)
#Write as ---> __init__ [TWO UNDERSCORES]
#2nd meaning of method = a function inside a class


#self is the key/first argument to this method
#Because it is a reference to the new objects created
#After self, you can add additional arguments

#After being defined, we store these arguments into fields in the object
#fields --> self.field_name
#And then you assign it a value
#Arguments inside a class function cannot be taken out that quick

class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #Birthday in mmddyyyy


account = User("John Doe", "14/7/2021")
print(account.name)
print(account.birthday)
