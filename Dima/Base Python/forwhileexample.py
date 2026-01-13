trueLogin='admin'
truePassword='1234'
autorization=False
count=0

while autorization==False:
    if count>=3:
        break
    print('Осталось попыток:',2-count)
    count=count+1
    login=input('login: ')
    if login=='root':
        print('root not resolvet')
        continue
    password=input('password: ')
    if login==trueLogin and password==truePassword:
        print('ok')
        autorization=True
    else:
        print('Ошибка.')

