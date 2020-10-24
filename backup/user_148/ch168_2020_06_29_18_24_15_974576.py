def login_disponivel(nome, lista):
    i = 0
    while i<len(lista):
        if not nome in lista:
            return nome
        else:
            nome = nome + str(i+1)
            return nome
        i += 1
