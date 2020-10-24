def quantos_uns(numero):
    i = 0
    um = 0
    while i < len(numero):
        if numero[i] == 1:
            um += 1
        i += 1
    return um

