def interseccao_valores(d1,d2):
    v1 = d1.values()
    lista = []
    for i in v1:
        if i in d2.values():
            lista.append(i)
            
    return lista