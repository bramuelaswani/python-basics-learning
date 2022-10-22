Fruits = ['Apple', 'Mango', 'Orange']
enumerateFruits = enumerate(Fruits)

print(type(enumerateFruits))

# converting to list
print(list(enumerateFruits))

# changing the default counter
enumerateFruits = enumerate(Fruits, 10)
print(list(enumerateFruits))


Fruits = ['Apple', 'Mango', 'Orange']

for item in enumerate(Fruits):
    print(item)

print('\n')
for count, item in enumerate(Fruits):
    print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(Fruits, 50):
    print(count, item)

x = ['op', 'gi', 'low', 'clodr', 'vol']
for count, item in enumerate(x, 10):
    print(count, item)
