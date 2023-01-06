# Very basic class
class MyClass:
  x = 5

print(MyClass) #Print Method 1

p1 = MyClass() #Print Method 2
print(p1.x)




# Class using __init__ function

  #Method 1

class Person:
  def __init__(self, names, ages):
    self.name = names
    self.age = ages

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

  #Method 2: Transform into str()

class Person2:
  def __init__(self, names, ages):
    self.name = names
    self.age = ages

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person2("Louie", 36)

print(p1)




# Object Methods

class Person3:
  def __init__(self, names, ages):
    self.name = names
    self.age = ages

  def function1(self):
    print("Hello my name is " + self.name)

p1 = Person3("Leon", 36)
p1.function1()




# Alternate to Self

class Person4:
  def __init__(mysillyobject, names, ages):
    mysillyobject.name = names
    mysillyobject.age = ages

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person4("Gizmo", 36)
p1.myfunc()
