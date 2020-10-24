def login_disponivel(user):
    lista_user = []
    if user not in lista_user:
        lista_user.append(user)
        return
    else:
        for p in range(len(lista_user)):
            user_novo = user+"[]".format(p)
            return user_novo