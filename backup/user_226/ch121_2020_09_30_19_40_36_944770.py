def subtracao_de_listas(a, b):
    i = 0
    lista = []
    while i < len(a):
        if a[i] not in b:
            lista.append(a[i])
        i += 1
    return lista