#Python Iterator


nums = (7, 8, 9, 5)

print(nums[1])

#You can print all values one by one by using Iterator

it = iter(nums)

print(it)

print(next(it))

print(next(it))

print(next(it))

# _next_ is an invil number






#Python Generator

#Generators are more instant and can do double than Iterators

#Yields make functions as generators

#Yield is like return but doesn't terminate functions

#This example is for squares

def topten():

    n = 1

    while n <= 10:
        aq = n*n
        yield aq
        n += 1

values = topten()

for i in values:
    print(i)
