login = input('Login?')
lista = []
while login != 'fim':
    if not login in lista:
        lista.append(login)
    else:
        i = 1
        k = True
        while k:
            login2 = login+str(i)
            if not login2 in lista:
                lista.append(login2)
                k = False
            i+=1
    login = input('Login?')   
    
for nome in lista:
    print(nome)