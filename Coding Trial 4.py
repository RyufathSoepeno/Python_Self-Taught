#List exercise

software = ["Android", "Microsoft", "IOS", "Linux"]

#Swapping lists

#Solution me

swap1 = software[0]
swap2 = software[1]

software[0] = swap2
software[1] = swap1

print(software)

#Solution Dojo

software[2], software[3] = software[3], software[2]
print(software)



