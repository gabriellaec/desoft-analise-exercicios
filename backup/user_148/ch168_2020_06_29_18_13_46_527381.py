def login_disponivel(nome, lista):
    i = 1
    while i<len(lista):
        if nome == lista[i]:
            nome = nome + str(i)
            i += 1
            return nome
        else:
            return nome