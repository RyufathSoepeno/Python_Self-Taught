#Filter, Map and Reduce


nmbs = (3, 2, 6, 8, 4, 6, 2, 9)

#Filter will filter your list and take your values
# ',' is pass
# '_' is indicating names for its internal use
# '_' is also a hint for programmers like you
#Filter (Functions, iterable/list)

def is_even(n):
    return n%2==0

evens = list(filter(is_even, nmbs))

print(evens)

#Lambda version

evens = list(filter(lambda n : n%2==0, nmbs))

print(evens)



#Map changes value on a list with commands

doubles = list(map(lambda m : m*2, evens))

print(doubles)



#Reduce takes value out to make it one, or more proportionate
#Reduce is not a list
#Reduce is a function Tools Module

from functools import reduce

def add_all(a, b):
    return a+b

sum = reduce(add_all, doubles)

print(sum)

#Lambda version

sum = reduce (lambda a, b : a+b, doubles)

print(sum)
