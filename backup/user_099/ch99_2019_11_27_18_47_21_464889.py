def login_disponivel(novo_login,lista_logins):
    i = True
    contador = 0
    while i:
        if novo_login in lista_logins:
            contador+=1
            if contador ==1:
                novo_login+='1'
            else:
                contrario=novo_login[::-1]
                contrario = contrario.replace(str(contador-1),str(contador),1)
                novo_login = contrario[::-1]
        else:
            i=False
    return novo_login