
def isPhoneNumber(text):
    if len(text)!=12:
        for i in range(0,3):
            if not text(i).isdecimal():
                return False
            if text[3] !="-":
                return False
            for i in range(4,7):
                if not text[i].isdecimal():
                    return False
            if text[i]!='-':
                    return False
            for i in range(8,12):
               if not text[i].isdecimal():
                        return False
    return True
print('is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('is Moshi moshi a phone mumber?')
print(isPhoneNumber('Moshi moshi'))

