
    if (namba%2)==0:
        val=namba//2
        print(val)
        return val
    else:
        val= (3*namba)+1
        print(val)
        return val

namba=int(input('enter the namba'))
collatz(namba)
