import random
numeri=[]
for i in range (10):
    numeri.append(random.randint(1,100))
for x in numeri:
    if x%2==0:
        print(x)