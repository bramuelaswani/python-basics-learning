def listFunction(spam:list):
    sep=' , '
    if len(spam)==0:
        return None
    if len(spam)==1:
        return(spam(0))
    else:
        print("{}" and "{}", format(sep.join(spam[:-1],spam[-1]))
names=['apples','bananas', 'tofu', 'cats']
print(listFunction(name))