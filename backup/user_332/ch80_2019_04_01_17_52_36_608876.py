def interseccao_chaves (dic1,dic2):
    lista = []
    for e in dic1:
        for i in dic2:
            if e == i:
                lista.append(e)
    return lista