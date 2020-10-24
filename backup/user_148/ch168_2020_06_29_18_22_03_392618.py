def login_disponivel(nome, lista):
    i = 0
    while i<len(lista):
        if nome != lista[i]:
            return nome
        else:
            nome += str(i)
            return nome
        i += 1
