def collatz(number):
 if (number% 2)==0:
     val=number//2
     print(val)
     return val
 else:
     val=3 * number+1
     print(val)
     return val

number=int(input('please Enter the number.'))
collatz(number)





