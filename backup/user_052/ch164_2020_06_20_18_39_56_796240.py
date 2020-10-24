def traduz (lista, dic):
    nova = []
    for i in dic:
        for e in lista:
            if i == e:
                nova.append(dic[i])
    return nova