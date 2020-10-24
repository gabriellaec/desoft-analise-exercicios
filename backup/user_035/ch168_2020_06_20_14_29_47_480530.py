def login_disponivel(user, lista_user):
    contador = 0
    if user not in lista_user:
        return user
    else:
        user = user+"{}".format(contador)
        contador +=1
        return user