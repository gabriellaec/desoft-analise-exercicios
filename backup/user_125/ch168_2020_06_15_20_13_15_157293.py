def login_disponivel(login,lista_registros):
a=0
    if login not in lista_registros:
        return login
    elif login in lista_registros:
        a=str(lista_registros.count(login))
        a+=1
        return login+a