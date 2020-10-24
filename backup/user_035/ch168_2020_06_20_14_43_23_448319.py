def login_disponivel(user, lista_user):
    if user not in lista_user:
        return user
    else:
        contador = 0
        for i in lista_user:
            if i[:len(user)] == user:
                contador +=1
                user = user+"{}".format(contador)
        return user