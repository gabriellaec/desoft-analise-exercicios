def login_disponivel(user, lista_user):
    if user not in lista_user:
        return user
    else:
        contador = 0
        for i in lista_user:
            if i[:len(user)] == user:
                contador +=1
        return user + "{}".format(contador)

verificador = True

lista_login = []

while verificador:
    pergunta = input("diga login : ")

    if pergunta == "fim":
        verificador = False
    else:
        lista_login.append(login_disponivel(pergunta, lista_login))

for i in lista_login:
    print(i)
