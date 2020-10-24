def login_disponivel(user, lista_user):
    if user not in lista_user:
        return user
    else:
        contador = 0
        for i in lista_user:
            if i[:len(user)] == user:
                contador +=1
        return user + "{}".format(contador)
user = "diga login : "
verificador = True
while verificador:
    lista_user = []
    if user == "fim":
        verificador = False
    else:
        login_disponivel(user, lista_user)
        verificador = False
for i in lista_user:
    print(lista_user[i])
