#Break, Continue and Pass statements

x = int(input("How many candies do you want ?"))

i = 1

while i <= x:
    print("Candy")
    i+=1

#To use limits

x = int(input("How many candies do you want again ?"))

available = 10

i = 1

while i <= x:
    if i>available:
        print("Out of stock")
        break
    print("Candy")
    i+=1

#"Break" is to mention the end of the limits but shows "all" of the limit

for i in range(1, 26):
    if i%3==0 :
        continue
    print (i)


#"Continue" will skip the remaining stops
#"And" includes two functions at the same time
#Which are divisible by both 5 and 3{15, 30}
#Not divsible by only 5, and only 3

for i in range(1, 26):
    if i%3==0 and i%5==0:
        continue
    print (i)


#"Pass" is similar like 'continue';
#But the result or mistake will still be shown (Usually to shorten lines)
#"!=" Means not equal

for i in range(1, 26):
    if(i%2!=0):
        pass
    else:
        print(i)
