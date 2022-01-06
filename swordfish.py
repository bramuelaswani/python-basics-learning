while True:
    print('Who are you?')
    name=input()
    if name!= 'joe':
        continue
    print('Hello, Joe. what is the password? (it is a fish)')
    password= input()
    if password == 'swordfish':
        print('Access granted.')
        break
    #continue
        