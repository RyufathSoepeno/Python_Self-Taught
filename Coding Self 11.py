#Data types in Python


#Numberic data

#They are : int, float, complex and bool

num = 5
print(type(num))

num = 7.
print(type(num))

num = 9+1
print(type(num))

num = 6+9j
print(type(num))

#converting numeric data

a = 5.6
b = int(a)
print(type(b))
print(b)

k = float(b)
print(k)

f = 8
c = complex(b, f)
print(c)

#Bool is Boolean, True or False

print(b<k)
print(type(b<k))


#Sequence data

world = [24, 49, 98, 65]
print(type(world))

world = (24, 49, 98, 65)
print(type(world))

world = {24, 49, 98, 65}
print(type(world))

#Python strings are iterable, which means they can be ordered

HRP = ("The Enemy Within")
print(type(HRP))

print(type("Falayon"))

print(type(range(7)))

#Dictionary and Mapping

h = {"Keitel" : "Jodl",  "Krebs" : "Burgdorf"}

print(h.keys())

print(h.values())

#Keys are an index number, so youneed to use square brackets

print(h["Krebs"])

#Or you can also use

print(h.get("Keitel"))





h.get("Burgdorf")

