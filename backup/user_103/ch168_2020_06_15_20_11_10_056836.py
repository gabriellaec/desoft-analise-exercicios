def login_disponivel(login,lista_registros):
    if login not in lista_registros:
        return login
    elif login in lista_registros:
        a=str(lista_registros.count(login))
        return login+a
    print(lista_registros)