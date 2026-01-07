#If Else statements

#If

a = 1
b = 2
# To print ("a is less than b")
#When pressing (:), it will go four spaces. Use it to structure the program
#Use (:) also to combine certain codes out of all the other codes

if a < b:
    print ("a is less than b")
print ("It is less")

if a > b:
    print ("a is more than b")
print ("Ok")

#The (:) run the condition of the if clause

a = 3
b = 2

if a < b:
    print ("a is less than b")
print ("It is not less")

if a > b:
    print ("a is more than b")
print ("Ok")

#Else (For the opposite/other statements)

d = 7
s = 8

if d < s:
    print("c is less than d")
else:
    print("c is not less than d")
print("Keep it up")

d = 10
s = 5

if d < s:
    print("c is less than d")
else:
    print("c is NOT less than d")
print("Keep it up")

#Elif (After Else, we get if) (Else is rather a final condition)
#The (=) is an assigned variable
#The (==) is an equal sign

r = 2
e = 3

if r < e:
    print("r is less than e")
elif r == e:
    print("r is equal to e")
else:
    print("r is not less than f")

r = 9
e = 3

if r < e:
    print("r is less than e")
elif r == e:
    print("r is equal to e")
else:
    print("r is not less than f")

#Elif is also similar to......
    
r = 3
e = 3

if r < e:
    print("r is less than e")
else:
    if r == e:
        print("r is equal to e")
    else:
        print("r is greater than e")
