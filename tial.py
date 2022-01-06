name = 'bbb'
while not name:
 print('Enter your name:')
name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests >3:
 print('Be sure to have enough room for all ' + str(numOfGuests)  + ' guests.')
print('Done')