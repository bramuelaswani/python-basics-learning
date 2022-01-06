import random
numberOfStreaks=0
coinFlip=[]
streak=0
for experiment in range(10000):
    for i in range (100):
        coinFlip.append(random.choice(['Head','Tail']))
        print(coinFlip)
    for i in range(len(coinFlip)):
        if coinFlip[i]==coinFlip[i-1]:
                streak +=1
        else:                streak=0
        if streak==6:
            numberOfStreaks+=1
            continue   
coinFlip=[]
print('chance of streak: %s%%' %(numberOfStreaks/100*10000))
