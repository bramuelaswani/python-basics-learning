'''thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1'''
import operator

q = [34, 29, 13, 32, 17, 6]
print(operator.itemgetter(-1)(q))
