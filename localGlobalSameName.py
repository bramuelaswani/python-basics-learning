def spam():
 eggs='spam local'
def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs= 'global'
bacon()
print(eggs)
