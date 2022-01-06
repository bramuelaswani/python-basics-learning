mypets=['zophie', 'pooka','Fat-tail']
print('Enter a pet name:')
name=input()
if name not in mypets:
    print('i do not have a pet named '  + name)
else:
    print(name + 'is my pet.')
    