import random 
number=int(input("Εισάγετε έναν αριθμό: "))
x=0
number1=0 
number2=1
Xn=0
if number<0:
  print("Ο αρηθμός που δώσατε είναι αρνητικός.")
elif number<=2:
 print("Ο όρος στην θέση",number,"δεν είναι πρώτος.")
else:
  for i in range(number-1):
    Xn=number1+number2 
    number1=number2
    number2=Xn
  for i in range(20):
    a=random.randint(0,99999999999)
    if (a**Xn)%Xn==(a%Xn):
      x+=1
    else:
      print("Ο όρος στην θέση",number,"δεν είναι πρώτος.")
      break   
  if x==20:
    print("Ο όρος στην θέση",number,"είναι πρώτος.")
