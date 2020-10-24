def login_disponivel(login,lista_registros):
    print(lista_registros)
    for i in range(len(lista_registros)):
        if login not in lista_registros:
            return login
        elif login in lista_registros or login+i:
            a=str(lista_registros.count(login))
            return login+a
