def login_disponivel(user, lista_user):
    if user not in lista_user:
        return user
    else:
        contador = 0
        contador +=1
        user = user+"{}".format(contador)
        return user