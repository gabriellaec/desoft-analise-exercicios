def traduz (lista, dic):
    nova = []
    for i in lista:
        if i in dic:
            nova.append(dic[i])
    return nova