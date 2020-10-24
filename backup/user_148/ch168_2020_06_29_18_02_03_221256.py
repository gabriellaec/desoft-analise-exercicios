def login_disponivel(nome, lista):
    i = 0
    while i<len(lista):
        if not nome in lista:
            return nome
        else:
            return nome + i
        i += 1
