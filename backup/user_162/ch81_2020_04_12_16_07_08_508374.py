def interseccao_chaves(D1):
    lista = []
    for i in D1:
        for j in i.values():
            lista.append(j)
        
    return lista