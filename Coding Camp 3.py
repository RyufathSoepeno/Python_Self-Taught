print ('== Absolute answer, = Answers is various/can change')

#To show a note without displaying
a,b=0,1
while a<10:
    print(a)
    a,b=b,a+b


a,b=0,1
while a<20:
    print (a)
    a,b=b, a+b

x=int(input("please enter an Integer"))
if x<0:
    x=0
    print ("Negative Changed To Zero")
elif x==0:
    print ("zero")
elif x==1:
    print ("one")
else:
    print ("more")



x=int(input('Number Please'))
if x % 2== 0:
    print('even')
else :
    print ('odd')


Animals = ('dog, Cat, Rabbit, Fish')
for any in Animals:
    print (any,len(any))
    
for real in range (7) :
    print ("yeehaw")
