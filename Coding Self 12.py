#Import Math Functions



#If you want to use them, you need to ask for them
#To that, we use modules to call in modules
#Module doesn't define a function
#Import - Module Name

import math

x = math.sqrt(25)
print(x)

#Floor = rounded to the least

#Ceil = rounded to the most

print(math.floor(2.9))

print(math.ceil(2.2))

print(math.pow(3, 2))

#To call in constant

print(math.pi)

print(math.e)


#If you want the module to be in another name

import math as m

print(m.sqrt(16))

#If you only want to import without naming the module

#"From' is an origin

#From - Module Name - Import - Modules

from math import sqrt, pow

print(pow(4, 5))

print(sqrt(9))
