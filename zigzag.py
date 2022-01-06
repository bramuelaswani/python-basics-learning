import time, sys
indet=0
indentIncreasing=True

try:
    while True:
        print(' ' * indet, end=' ')
        #print(' ***')
        time.sleep(0.1)
        if indentIncreasing:
         indet=indet+1
        if indet==20:
         indentIncreasing= False
        else:
         indet=indet-1
        if indet==0:
         indentIncreasing=True
except KeyboardInterrupt:
 sys.exit