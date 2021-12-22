#Loops in Python

#The long way

a = ["Android", "Microsoft", "IOS", "Linux"]

print(a[0])
print(a[1])
print(a[2])
print(a[3])


#Using for loops. [Limited]

for element in a:
    print(element)

#Finding sums using lists
#Variable is original is 0
#But since it is a variable inside a variable, the old answer is inside
#So it is 'zero' + 'looped e'. And the addition of the variable is looped

b = [20, 10, 5]

variable = 0

for e in b:
    variable = variable + e
print(variable)
print("That is the total from =")
print(b)

#Using range. It is (Beginning, end)
#Use 'list' to list things when they are not in the list functions

c = list(range(1, 5))
print(c)

for i in range(1, 5):
    print(i)

add = 0

for i in range(1, 5):
    add = add + i

print(add)

#How to add certain values on the range

print(list(range(1, 8)))

#Let's say only multiples of three
#Use modul operator '%'

three = 0

for divide in range(1, 8) :
    if divide % 3 == 0:
        three = three + divide
print(three)
    

