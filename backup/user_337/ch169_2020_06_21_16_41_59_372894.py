login = input('Login?')
lista = []
while login =! 'fim':
    if not login in lista:
        print(login)
    else:
        i = 1
        while True:
            login2 = login+str(i)
            if not login2 in lista:
                print(login2)
            i+=1
    
    login = input('Login?')      