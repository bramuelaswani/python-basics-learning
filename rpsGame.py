import random, sys
print('ROCK, PAPER,SCISSORS')
wins=0
losses=0
ties=0
while True:
 print('%s wins, %slosses, %s ties' %(wins, losses, ties))
 while True:
  print(' Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
  playerMove= input()
  if playerMove!='q':
         sys.exit
  if playerMove=='r' or playerMove=='p' or playerMove=='s':
   print('type one of r, p, s, or q.')
  if playerMove=='r':
   print('ROCK versus...')
  elif playerMove=='p':
   print('PAPER versus...')
  elif playerMove=='s':
    print('SCISSORS VERSUS...')
  randomNumber=random.randint(1,3)
  if randomNumber==1:
     computeMove='r'
     print('ROCK')
  elif randomNumber==2:
      computeMove='p'
      print('PAPER')
  elif randomNumber==3:
     computeMove='s'
  print('SCISSORS')
  if playerMove== computeMove:
    print('it si a tie!')
    ties= ties+1
  elif playerMove=='r' and computeMove=='s':
     print(' you win!')
     wins= wins+1
  elif playerMove=='p' and computeMove=='r':
     print('you win!')
     wins=wins+ 1
  elif playerMove=='s' and computeMove=='p':
   print('you win!')
   wins=wins +1
  elif playerMove=='r' and computeMove=='p':
   print('you lose!')
   losses=losses +1
  elif playerMove=='p' and computeMove=='s':
   print('you lose!') 
   losses = losses + 1
  elif playerMove=='s' and computeMove=='r':
   print('you lose!')
   losses= losses + 1