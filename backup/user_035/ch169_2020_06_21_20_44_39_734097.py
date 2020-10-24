def login_disponivel(user, lista_user):
    if user not in lista_user:
        return user
    else:
        contador = 0
        for i in lista_user:
            if i[:len(user)] == user:
                contador +=1
        return user + "{}".format(contador)
pergunta = "diga login : "
verificador = True
lista_login = []
while verificador:
    if pergunta == "fim":
        verificador = False
    else:
        login_disponivel(pergunta, lista_login)
        lista_login.append(pergunta)
for i in lista_login:
    print(lista_login[i])
