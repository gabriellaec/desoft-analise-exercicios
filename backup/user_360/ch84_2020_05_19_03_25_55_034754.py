def inverte_dicionario(dic):
    dic2 = {}
    for i in dic.values():
        if i not in dic2.keys():
            lista = []
            for j in dic.keys():
                if dic[j] == i:
                    lista.append(j)
            dic2[i] = lista
    return dic2