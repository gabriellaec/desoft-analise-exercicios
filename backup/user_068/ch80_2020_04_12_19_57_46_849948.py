def interseccao_chaves(a, b):
    lista = []
    for i in a.keys():
        if a[i] == b.keys():
            lista.append(a)
    return lista
print(lista)