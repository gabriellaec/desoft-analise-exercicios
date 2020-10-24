login = input('Login?')
lista = []
while login != 'fim':
    if not login in lista:
        lista.append(login)
    else:
        i = 1
        while True:
            login2 = login+str(i)
            if not login2 in lista:
                lista.append(login2)
                False
            i+=1
    login = input('Login?')   
    
for nome in lista:
    print(nome)