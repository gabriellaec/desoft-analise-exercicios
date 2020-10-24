def interseccao_valores(d1, d2):
    lista1 = []
    for k,v in d1.items():
        lista1.append(v)
    lista2 = []
    for i in d2:
        x = d2[i]
        for y in lista1:
            if x == y:
                lista2.append(x)
        return lista2