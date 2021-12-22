#Arrays


#Arrays = Value of same type
#arrays dont have specific size, which means you can expand or shrink it

import array as a

#('Type of Arrays', Value)
#Type of Arrays can be seen on google, there are lots of them

vals = a.array('i', [5,9,8,-4,2])

print(vals)

#To know the size of an array

print(vals.buffer_info())

# Result = (Adress, size)

#To get values one by one
#Pay attention on the brackets

for i in range(5):
    print(vals[i])



