def login_disponivel(nome, lista):
    i = 1
    while i<len(lista):
        if nome != lista[i]:
            return nome
        else:
            nome = nome + str(i)
            i += 1