def login_disponivel(login,lista_registros):
    lista=[]
    if login not in lista_registros:
        return login
    else:
        for i in range(len(lista_registros)):
            user = str(lista_registros[0:len(login):1])
            if user == login:
                lista.append(user)
    print(lista)
   