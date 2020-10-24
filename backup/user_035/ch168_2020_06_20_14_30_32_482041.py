def login_disponivel(user, lista_user):
    contador = 0
    if user not in lista_user:
        return user
    else:
        contador +=1
        user = user+"{}".format(contador)
        return user