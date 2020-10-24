def traduz (lista, dic):
    nova = []
    for i in lista:
        for o in dic:
            if i == o:
                nova.append(dic[o])
    return nova