def login_disponivel(login,lista_registros):
    login= input('Qual é o seu login?')
    while login != 'fim':
        login= input('Qual é o seu login') 
    if login not in lista_registros:
        return login
    else:
        for i in range(len(lista_registros)):
            lista=[]
            user = str(lista_registros[i][0:len(login):1])
            if user == login:
                lista.append(user)
        print (user+str(len(lista)))


      