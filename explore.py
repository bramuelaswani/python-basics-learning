print(1+2+3.0)
a=[58,45,12]
a=a.append(7)
print(a)
print(float(4))
print('2'*2)
print('2'+'2')
b={"craig":10,"sizwe":20}
print(list(b.keys()))
my_Set={2,5,6,6,7,2,4}
print(my_Set)
name=['joe','ken',"soap","joe"]
for i in name:
    i.upper()
print(name)

count = 1

while True:

    if count%2 == 0:

        break

    print(count)

    count += 1

n = 1

while True:

    if n%0O6 == 0:

        break

    print(n)

    n += 1




# None = True

# while True:

#     print(None)

#     break

x = (i for i in range(3))

for i in x:

    print(i)

for i in x:

    print(i)

# def multiply(x,y):

#     return x*y

# multiply()

# def divide(x,y)

#     return x/y 

# divide(6,3)

def equate(x,y): 

      return (x^y)/8 
print(equate(2,64))

def factorial(n):

      if n == 1: 

          return n

      else: 

          return n * factorial(n-1)
print(factorial(6))

n = 12

def func():

    global n

    print('Value of n is', n)

    n = 7

    print('Changed global n to', n)

func()

print('Value of n is now', n)

explorer = ['irvine', 'marko', 'salamander', 'wisani', 'robyn', 'joanne']

for i in range(len(explorer)):

    if explorer[i][-2] == 'n' and (explorer[i][1] == 'a' or explorer[i][-3] == 'a'):

        print(explorer[i])

explore_string ='My cat likes watching television!'

#k = [print(x) for x in explore_string if x not in "aeiou"]
i=[12, 75, 87, 1, 3, 8, 0, 17, 24, 80, 27]
i.sort
print(1)

A=6
B=15
print(A % B/A // (A/B))

a = [58, 45, 12]
print(a.insert(3, 10))
