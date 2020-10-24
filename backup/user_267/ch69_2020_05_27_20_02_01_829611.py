def junta_listas(a):
    lista = []
    for i in a:
        w = 0
        while w <= len(i):
            lista.append(i[w])
            w += 1
    return lista
   