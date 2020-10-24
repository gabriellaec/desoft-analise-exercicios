def quantos_uns(x):
    i = 0
    lista = []
    while i < len(x):
        if x[i] == '1':
            lista.append(x[i])
        i += 1
    return len(lista)
        