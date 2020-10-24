def monta_dicionario(lista1,lista2):
    dic = {}
    for v in lista1:
        for k in lista2:
            dic[k] = v
    return dic
        