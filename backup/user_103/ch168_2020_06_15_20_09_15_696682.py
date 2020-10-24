def login_disponivel(login,lista_registros):
    if login not in lista_registros:
        return login
    elif login in lista_registros:
        a=lista_registros.count(login)
        b= str(a+1)
        return login+b
    