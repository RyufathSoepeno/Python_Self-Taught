#For vs While loop


#Both loops can counter the control pof the loop peretitions
#Both can be done for ANY loop

#For loop is done automitacally

#While loop must be done explicitly,
#Which means "while" ]it needs counters, another variable


#Examples with same result

count = 1

while count <= 10:
    value = count*4
    print(value, end = " ")
    count += 1

for i in range(1, 11):
    value = i*4
    print(value, end = " ")
