def spam(devideBy):
    return 42/ devideBy
try: #erase this
 print(spam(2))
 print(spam(12))
 print(spam(0))
 print(spam(1))
except ZeroDivisionError: #and this
    print(' Error: Invalid argument.') #this it just saves the comp from several excuses