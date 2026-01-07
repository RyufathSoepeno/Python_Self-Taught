#Swapping Two Variables

S1 = "Area 51"
S2 = "Area 69"

print (S1)
print (S2)

#Usually, we rewrite our strings to swap, but it is not effective so....


#mistake 1
# S1 = "Area 69"
# S2 = "Area 51"

#mistake 2
# S1 = S2
# S2 = S1


#Solution 1. It can be any other than temp

temp  = S1
tempt  = S2

S1 = tempt
S2 = temp 

print (S1)
print (S2)

#Solution 2. Swapped from solution 1

temp = S1
S1 = S2
S2 = temp

print (S1)
print (S2)
