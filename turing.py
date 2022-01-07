print("welcome to TURING".capitalize())
# x="abcdef"
# i="a"
# while i in x[:-1]:
#     print(i,end=" ")

data=[1,2,3]
def incr(x):
    return x+1
print(list(map(incr,data)))

# y=[2,5J,6]
# y.sort()
# print(y)

def f(x,l=[]):
    for i in range(x):
        l.append(i*1)
    print(l)
print(f(2))
print(f(3,[3,2,1]))
print(f(3))

d={40:"jphn",34:"hhh"}
print(d)

array=["welcome","to","turig"]
print("-".join(array))


import re
res=re.findall("welcomee to turing","welcome",1)
print(res)

print([i.lower() for i in "TURING"])
