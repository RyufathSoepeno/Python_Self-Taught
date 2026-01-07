import random
#You learned most of these by yourself, be proud of it :-=)


r = random.random()
print(r)
#This method prints out random numbers from 0.0 - 1.0

i = random.randint(0, 1000)
print("In this lucky wheel, you'll earn", i, "dollars")
#random.randint(a, b) = b < num < a
#random can also be done using negative signs

d = random.randrange(20, 120, 4)
print(d)
#random.randrange(start, stop, step)
#range(start, stop, step)
#Step is the dividend
#Start >= Step if want to be divisible
#It can also be done using random.randrange(start, stop)

randomList = []
for i in range(0, 6):
    randomList.append(random.randrange(50, 5000, 5))

print(randomList)
#Append = Adding

x = random.sample(range(9, 51), 5)
print("Before Sorted")
print(x)
#random.sample(range, how many list)
#random.sample functions to take out numbers without duplicates

x.sort()
print("After Sorting")
print(x)




