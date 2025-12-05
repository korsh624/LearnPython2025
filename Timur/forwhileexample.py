trueLogin='admin'
truePassword='1234'
autorization=False

while autorization==False:
    login=input('login: ')
    password=input('password: ')
    if login==trueLogin and password==truePassword:
        print('ok')
        autorization=True
    else:
        print('fail')
