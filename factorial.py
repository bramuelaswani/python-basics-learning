def factorial(num):
    factorial=1
    if num<0:
        print('please input a posiive number')
    if num==0:
        print(f'the factorial of {num} if {factorial}')
    else:
        for i in range(1, num+1):
            factorial*=i
    return f'The factorial of { num } is { factorial }'

num=int(input('plese input a number to calculate the factorial'))
print(factorial(num))
