def login_disponivel(nome, lista):

    numero = 0
    nome_0 = nome
    for login in lista:
        if nome == login:
            numero += 1
            nome = login  + str(numero)


    login_final = nome_0 + str(numero)

    if numero > 0:
        return login_final
    else:
        return nome_0