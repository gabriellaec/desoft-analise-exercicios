def interseccao_valores (dic1, dic2):
    lista = []
    for valor in dic1 .values():
        if valor in dic2 .values():
            lista.append (valor)
    return lista    
    