import math as mt
my_dict = {"A": 1}
my_dict["A"] = 2

print(my_dict)

print(mt.exp(1))
print(12+2*24/3*4+4)

for num in range(10, 12):
    for j in range(9, num):
        print(num*j)


def func(x, y):
    if x == 0:
        return y
    else:
        return func(x-1, x-y)


print(func(4, 7))

set = (2, 5, 7)
print(set[-1])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i+5 for i in nums if i % 2]
print(x)


# print("Hello World"[:::-1]

# se2 = {3, 4, 2, 3, 1}
# print(se2)

# a = {3, 4, 2, 3, 1}
# print(a)

# x=3
# while x<11:
#     if x%2==0:
#         x=x-1
#     else:
#         x=x*2
#     print(x)

dict1 = {"key":  "A", "key2": 2}
dict2 = {"key2":  2, "key": "A"}
print(dict1 == dict2)

print((1+2**2)**(1+1)*2)

for letter in "Hello there":
    i = letter
print(i)

set1 = {"stock", "bond", "option"}
# print(set1[-1])


x = [2, [1]]
y = list(x)
x[0] = -1
x[1][0] = -1
y = list(x)

print(y)
