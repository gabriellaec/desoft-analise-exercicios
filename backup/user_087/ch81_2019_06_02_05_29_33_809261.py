def interseccao_valores(d1, d2):
    lista = []
    lista1 = []
    lista2 = []
    for c1 in d1:
        k1 = d1[c1]
        lista1.append(k1)
    for c2 in d2:
        k2 = d2[c2]
        lista2.append(k2)	
    for n in lista1:
        if n in lista2:
            lista.append(n)
    return lista