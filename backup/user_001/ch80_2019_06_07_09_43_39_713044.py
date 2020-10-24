def interseccao_valores(dic1,dic2):
    lista = []
    for k in dic1:
        for keys in dic2:
            if k==keys and keys not in lista:
                lista.append(keys)
    return lista