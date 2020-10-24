def interseccao_chaves(d1, d2):
    lista = []
    lista1 = []
    lista2 = []
    for c1 in d1:
        lista1.append(c1)
    for c2 in d2:
        lista2.append(c2)	
    for n in lista1:
        if n in lista2:
            lista.append(n)
    return lista