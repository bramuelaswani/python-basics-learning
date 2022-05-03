n = int(input())
for i in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print("n, 'equals'', n//x")
            break
        else:
            # loop fell through without fimding a factor
            print(n, 'is a prime number')
