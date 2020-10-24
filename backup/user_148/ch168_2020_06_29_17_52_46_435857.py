def login_disponivel(nome, lista):
    i = 0
    while i<len(lista):
        if lista[i] != nome:
            return nome
        else:
            return nome.append(i)
        i += 1
