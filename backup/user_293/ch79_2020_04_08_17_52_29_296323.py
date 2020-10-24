def monta_dicionario(lista_1,lista_2):
    dic = {}
    i = 0
    for e in lista_1:
        dic[e] = lista_2[i]
        i += 1
    return dic