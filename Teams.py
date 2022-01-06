import random, sys
Teams=['Arsenal', 'manchester united', 'liverpool', 'chelsea', 'manchester city']
TeamPosition=0
for name in Teams:
    if name=='Arsenal':
        break
    TeamPosition= TeamPosition + 1
print('Arsenal', + TeamPosition)
TeamPosition=0
for name in Teams:
    if name== 'manchester united':
        break
    TeamPosition= TeamPosition +1 
    print('manchester united', + TeamPosition)
    TeamPosition=0
for name in Teams:
    if name== 'liverpool':
        break
    TeamPosition=TeamPosition + 1
    print('liverpool', TeamPosition)
TeamPosition=0
for name in Teams:
    if name== 'chelsea':
        break
    TeamPosition=TeamPosition + 1
    print('chelsea', + TeamPosition)
    

