def apaga_repetidos(palavra):
    lista = []
    u = 0
    for i in palavra:
        if i not in lista:
            lista.append(i)
        if palavra[u] in lista:
            palavra[u] = '*'
        u += 1
    return palavra