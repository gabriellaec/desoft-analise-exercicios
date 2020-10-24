def login_disponivel(nome, lista):
    i = 0
    while i<len(lista):
        if nome != lista[i]:
            return nome
        else:
            return nome + str(i)
        i += 1
