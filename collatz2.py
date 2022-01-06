def collatz(num):
 if (num // 2)==0:
     val=num//2
     print(val)
     return val
 else:
     val=(3 * num) + 1
     print(val)
     return val

count=0
while count<5:
 num=int(input('enter the number'))
 val=collatz(num)
 print (val)
collatz(num)

