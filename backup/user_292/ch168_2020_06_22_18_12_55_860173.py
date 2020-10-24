def login_disponivel(nome, lista):
    for i in lista:
        if nome not in lista:
            return nome
        if i == nome:
            nome = nome + str(1)
        lista_nova = []
        for n in lista:
            lista_nova.append(n[:-1])
        c = 1
        for z in lista_nova:
            if z == nome:
                c += 1
        nome = nome + str(c)
    return nome