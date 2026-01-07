#Simple BMI calculator

name = "Shenzen"
height_m = 4
weight_kg = 5

#The ** is powers of

bmi = weight_kg / (height_m ** 2)

print("bmi is ")
print(bmi)

if bmi < 25 :
    print(name)
    print("It is not overweight")
else:
    print(name)
    print("He is overweight")

print("Alternate silly answer is")
    
name = "Shenzen"
height_m = 4
weight_kg = 1200

bmi = weight_kg / (height_m ** 2)

print("bmi is ")
print(bmi)

if bmi < 25 :
    print(name)
    print("It is not overweight")
else:
    print(name)
    print("He is overweight")
