def traduz (lista, dic):
    nova = []
    for i in dic:
        for e in lista:
            if e in dic:
                nova.append(dic[i])
    return nova