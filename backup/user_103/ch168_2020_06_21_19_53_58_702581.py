def login_disponivel(login,lista_registros):
    if login not in lista_registros:
        return login
    else:
        lista=[]
        for i in range(len(lista_registros)):
            user = str(lista_registros[i][0:len(login):1])
            if user == login:
                lista.append(user)
        return user+str(len(lista))
   
