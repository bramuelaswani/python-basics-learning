def commaCode(spam:list):
    sep=','
    if len(spam)==0:
        return None
    if len(spam)==1:
        return spam[0]
    else:
        return "{} and {}".format(sep.join(spam[:-1]),spam[-1])

names = ['apples','bananas','tofu','cats']
print(commaCode(names[:]))
