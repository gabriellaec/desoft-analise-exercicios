def monta_dicionario(lista1,lista2):
    dic = {}
    for k in lista1.keys():
        for v in lista2.values():
            dic[k] = v
    return dic
        