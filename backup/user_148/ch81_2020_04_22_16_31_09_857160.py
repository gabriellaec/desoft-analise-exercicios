def interseccao_valores(d1, d2):
    lista = []
    
    for v1 in d1.values():
        for v2 in d2.values():
            if v1 == v2:
                lista.append(v1)
    
    return lista