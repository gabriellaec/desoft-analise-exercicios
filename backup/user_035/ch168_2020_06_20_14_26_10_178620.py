def login_disponivel(user):
    lista_user = []
    contador = 0
    if user not in lista_user:
        lista_user.append(user)
        return
    else:
        for p in range(len(lista_user)):
            user = user+"{}".format(contador)
            contador +=1
            return